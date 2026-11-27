import { Buffer } from "node:buffer";
import { Webhook } from "standardwebhooks";
import { describe, expect, test } from "vitest";

import { RepalisError } from "./base";
import {
  RepalisWebhookError,
  RepalisWebhookUnknownTypeError,
  RepalisWebhookVerificationError,
  validateWebhook,
} from "./webhooks";

interface DummyPayload {
  type: "dummy.event";
  value: string;
}

const secret = "test-secret";
const base64Secret = Buffer.from(secret, "utf8").toString("base64");
const eventTypes = new Set(["dummy.event"]);

const getHeaders = (body: string, timestamp: Date = new Date()): Record<string, string> => {
  const signature = new Webhook(base64Secret).sign("test-webhook", timestamp, body);
  return {
    "Webhook-Id": "test-webhook",
    "Webhook-Timestamp": String(Math.floor(timestamp.getTime() / 1000)),
    "Webhook-Signature": signature,
  };
};

const validateEvent = (
  body: string | Uint8Array,
  headers: Record<string, string>,
): Promise<DummyPayload> => {
  return validateWebhook<DummyPayload>(body, headers, secret, eventTypes);
};

describe("validateWebhook", () => {
  test.each([
    ["string", (body: string) => body],
    ["Buffer", (body: string) => Buffer.from(body)],
    ["Uint8Array", (body: string) => new TextEncoder().encode(body)],
  ])("validates a known event from a %s", async (_type, getRawBody) => {
    const body = JSON.stringify({ type: "dummy.event", value: "payload" });

    await expect(validateEvent(getRawBody(body), getHeaders(body))).resolves.toEqual({
      type: "dummy.event",
      value: "payload",
    });
  });

  test("validates a Standard Webhooks-formatted secret", async () => {
    const key = globalThis.crypto.getRandomValues(new Uint8Array(32));
    const secret = `whsec_${Buffer.from(key).toString("base64")}`;
    const body = JSON.stringify({ type: "dummy.event", value: "payload" });
    const timestamp = new Date();
    const signature = new Webhook(secret).sign("test-webhook", timestamp, body);
    const headers = {
      "Webhook-Id": "test-webhook",
      "Webhook-Timestamp": String(Math.floor(timestamp.getTime() / 1000)),
      "Webhook-Signature": signature,
    };

    await expect(validateWebhook<DummyPayload>(body, headers, secret, eventTypes)).resolves.toEqual(
      {
        type: "dummy.event",
        value: "payload",
      },
    );
  });

  test("rejects an invalid signature", async () => {
    const body = JSON.stringify({ type: "dummy.event", value: "payload" });

    await expect(validateEvent(body, getHeaders("{}"))).rejects.toThrow(
      RepalisWebhookVerificationError,
    );
  });

  test("rejects malformed signature encoding", async () => {
    const body = JSON.stringify({ type: "dummy.event", value: "payload" });
    const headers = getHeaders(body);
    headers["Webhook-Signature"] = "v1,not-base64!";

    await expect(validateEvent(body, headers)).rejects.toThrow(RepalisWebhookVerificationError);
  });

  test("rejects missing headers", async () => {
    const body = JSON.stringify({ type: "dummy.event", value: "payload" });

    await expect(validateEvent(body, {})).rejects.toThrow(RepalisWebhookVerificationError);
  });

  test("rejects a stale timestamp", async () => {
    const body = JSON.stringify({ type: "dummy.event", value: "payload" });
    const timestamp = new Date(Date.now() - 6 * 60 * 1000);

    await expect(validateEvent(body, getHeaders(body, timestamp))).rejects.toThrow(
      RepalisWebhookVerificationError,
    );
  });

  test("rejects an unknown event type", async () => {
    const body = JSON.stringify({ type: "future.event", value: "payload" });

    try {
      await validateEvent(body, getHeaders(body));
      throw new Error("Expected validateEvent to throw");
    } catch (error) {
      expect(error).toBeInstanceOf(RepalisWebhookUnknownTypeError);
      expect((error as RepalisWebhookUnknownTypeError).eventType).toBe("future.event");
    }
  });

  test("wraps malformed signed payloads", async () => {
    const body = "{";

    await expect(validateEvent(body, getHeaders(body))).rejects.toThrow(RepalisWebhookError);
  });

  test("uses the Repalis webhook error hierarchy", () => {
    expect(new RepalisWebhookError("error")).toBeInstanceOf(RepalisError);
    expect(new RepalisWebhookVerificationError("error")).toBeInstanceOf(RepalisWebhookError);
    expect(new RepalisWebhookUnknownTypeError("future.event")).toBeInstanceOf(RepalisWebhookError);
  });
});
