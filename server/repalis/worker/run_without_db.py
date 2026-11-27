import dramatiq

from repalis.worker._broker import get_broker
from repalis.worker._encoder import JSONEncoder

# Entrypoint for workers whose queues never touch PostgreSQL. Building the broker
# without the SQLAlchemy middleware avoids creating a database engine/pool the
# worker would never use. The broker must be set as the global broker before
# `repalis.tasks` is imported, so actors are declared against it rather than the
# default (database-backed) broker created by `repalis.worker`.
broker = get_broker(database=False)
dramatiq.set_broker(broker)
dramatiq.set_encoder(JSONEncoder(broker))

from repalis import tasks
from repalis.logfire import configure_logfire
from repalis.logging import configure as configure_logging
from repalis.posthog import configure_posthog
from repalis.sentry import configure_sentry

configure_sentry()
configure_logfire("worker")
configure_logging(logfire=True)
configure_posthog()

__all__ = ["broker", "tasks"]
