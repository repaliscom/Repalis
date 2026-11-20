import { RepalisError } from "./base";

const webhookToleranceSeconds = 5 * 60;

export class RepalisWebhookError extends RepalisError {
  constructor(message: string, options?: ErrorOptions) {
    super(message, options);
    this.name = "RepalisWebhookError";
  }
}

export class RepalisWebhookVerificationError extends RepalisWebhookError {
  constructor(message: string, options?: ErrorOptions) {
    super(message, options);
    this.name = "RepalisWebhookVerificationError";
  }
}

export class RepalisWebhookUnknownTypeError extends RepalisWebhookError {
  constructor(public readonly eventType: string | null) {
    super(`Unknown webhook event type: ${JSON.stringify(eventType)}`);
    this.name = "RepalisWebhookUnknownTypeError";
  }
}

export const validateWebhook = async <Payload>(
  body: string | Uint8Array,
  headers: Record<string, string>,
  secret: string,
  eventTypes: ReadonlySet<string>,
): Promise<Payload> => {
  const bodyText = typeof body === "string" ? body : new TextDecoder().decode(body);
  await verifySignature(bodyText, headers, secret);

  let parsed: unknown;
  try {
    parsed = JSON.parse(bodyText);
  } catch (error) {
    throw new RepalisWebhookError("Failed to parse webhook payload", {
      cause: error,
    });
  }

  const eventType =
    typeof parsed === "object" &&
    parsed !== null &&
    "type" in parsed &&
    typeof parsed.type === "string"
      ? parsed.type
      : null;
  if (eventType === null || !eventTypes.has(eventType)) {
    throw new RepalisWebhookUnknownTypeError(eventType);
  }

  return parsed as Payload;
};

const verifySignature = async (
  body: string,
  headers: Record<string, string>,
  secret: string,
): Promise<void> => {
  if (secret.length === 0) {
    throw new RepalisWebhookVerificationError("Secret can't be empty");
  }

  const normalizedHeaders = Object.fromEntries(
    Object.entries(headers).map(([key, value]) => [key.toLowerCase(), value]),
  );
  const webhookId = normalizedHeaders["webhook-id"];
  const webhookTimestamp = normalizedHeaders["webhook-timestamp"];
  const webhookSignature = normalizedHeaders["webhook-signature"];
  if (!webhookId || !webhookTimestamp || !webhookSignature) {
    throw new RepalisWebhookVerificationError("Missing required headers");
  }

  const timestamp = Number(webhookTimestamp);
  if (!Number.isFinite(timestamp)) {
    throw new RepalisWebhookVerificationError("Invalid signature headers");
  }

  const now = Date.now() / 1000;
  if (timestamp < now - webhookToleranceSeconds) {
    throw new RepalisWebhookVerificationError("Message timestamp too old");
  }
  if (timestamp > now + webhookToleranceSeconds) {
    throw new RepalisWebhookVerificationError("Message timestamp too new");
  }

  const signedContent = `${webhookId}.${Math.floor(timestamp)}.${body}`;
  const textEncoder = new TextEncoder();
  const signedContentBytes = textEncoder.encode(signedContent);
  const signingKeys = await Promise.all(
    hmacKeys(secret).map((key) =>
      globalThis.crypto.subtle.importKey("raw", key, { name: "HMAC", hash: "SHA-256" }, false, [
        "verify",
      ]),
    ),
  );

  for (const versionedSignature of webhookSignature.split(" ")) {
    const [version, signature] = versionedSignature.split(",", 2);
    if (version !== "v1" || signature === undefined) {
      continue;
    }
    const decodedSignature = decodeBase64(signature);
    if (decodedSignature === null) {
      continue;
    }
    for (const signingKey of signingKeys) {
      if (
        await globalThis.crypto.subtle.verify(
          "HMAC",
          signingKey,
          decodedSignature,
          signedContentBytes,
        )
      ) {
        return;
      }
    }
  }

  throw new RepalisWebhookVerificationError("No matching signature found");
};

const hmacKeys = (secret: string): BufferSource[] => {
  const utf8Key = new TextEncoder().encode(secret);
  const keys: BufferSource[] = [utf8Key];
  const remainder = secret.startsWith("whsec_") ? secret.slice("whsec_".length) : secret;
  const decoded = decodeBase64(remainder);
  if (decoded !== null && decoded.byteLength > 0 && !bytesEqual(decoded, utf8Key)) {
    keys.push(decoded);
  }
  return keys;
};

const bytesEqual = (left: Uint8Array, right: Uint8Array): boolean => {
  if (left.byteLength !== right.byteLength) {
    return false;
  }
  for (let index = 0; index < left.byteLength; index++) {
    if (left[index] !== right[index]) {
      return false;
    }
  }
  return true;
};

const decodeBase64 = (value: string): Uint8Array<ArrayBuffer> | null => {
  try {
    const decodedValue = globalThis.atob(value);
    const bytes = new Uint8Array(new ArrayBuffer(decodedValue.length));
    for (let index = 0; index < decodedValue.length; index++) {
      bytes[index] = decodedValue.charCodeAt(index);
    }
    return bytes;
  } catch {
    return null;
  }
};
