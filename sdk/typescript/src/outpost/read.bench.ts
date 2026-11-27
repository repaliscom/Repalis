import { afterAll, beforeAll, bench, describe } from "vitest";

import { CREDIT_REDUCER, REDUCER, SNAPSHOT } from "./benchmark";
import { Outpost } from "./client";
import {
  startRepalisServer,
  startRedisServer,
  type RepalisServer,
  type RedisServer,
} from "./testing";

const meter = { meter_id: "meter", external_customer_id: "alice" };

let redisServer: RedisServer;
let repalis: RepalisServer;
let outpost: Outpost;

beforeAll(async () => {
  redisServer = await startRedisServer();
  repalis = await startRepalisServer([REDUCER, CREDIT_REDUCER], SNAPSHOT);
  outpost = await new Outpost(redisServer.socket, { client: repalis.client }).start();
  await outpost.actor({ external_customer_id: meter.external_customer_id });
  if ((await outpost.meter(meter))?.credited_units !== SNAPSHOT.sum)
    throw new Error("The warm read benchmark needs a ready meter");
});

afterAll(async () => {
  await outpost?.close();
  await repalis?.stop();
  await redisServer?.stop();
});

describe("meter", () => {
  bench("read a warm meter", async () => {
    await outpost.meter(meter);
  });
});
