import { RepalisError } from "../base";

export class RepalisOutpostError extends RepalisError {}
/** A read Outpost cannot answer yet: Repalis has not sent the configuration or the snapshot in time. */
export class NotReadyError extends RepalisOutpostError {}
export class UnavailableRedisError extends RepalisOutpostError {
  constructor(options?: ErrorOptions) {
    super("Redis is unavailable", options);
  }
}
export class MissingExternalIdError extends RepalisOutpostError {
  constructor() {
    super("Outpost needs an external_id on every event");
  }
}
export const redisUnavailable = (error: unknown): UnavailableRedisError =>
  new UnavailableRedisError({ cause: error });
export const isRedisConnectionError = (error: unknown): boolean => {
  if (error instanceof UnavailableRedisError) return isRedisConnectionError(error.cause);
  return (
    error instanceof Error &&
    (error.name === "MaxRetriesPerRequestError" ||
      [
        "ECONNABORTED",
        "ECONNREFUSED",
        "ECONNRESET",
        "EHOSTUNREACH",
        "ENETUNREACH",
        "ENOTFOUND",
        "EPIPE",
        "ETIMEDOUT",
        "EAI_AGAIN",
      ].includes((error as NodeJS.ErrnoException).code ?? "") ||
      [
        "Command timed out",
        "Connection is closed.",
        "Stream isn't writeable and enableOfflineQueue options is false",
      ].includes(error.message))
  );
};

/** Repalis answered 401 or 403: nothing Outpost asks will pass until the token does. */
export class RefusedError extends RepalisOutpostError {
  constructor(message = "Repalis refused Outpost") {
    super(message);
  }
}
