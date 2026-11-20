from repalis import tasks
from repalis.logfire import configure_logfire
from repalis.logging import configure as configure_logging
from repalis.posthog import configure_posthog
from repalis.sentry import configure_sentry
from repalis.worker import broker

configure_sentry()
configure_logfire("worker")
configure_logging(logfire=True)
configure_posthog()

__all__ = ["broker", "tasks"]
