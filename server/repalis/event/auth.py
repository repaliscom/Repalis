from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import (
    Agent,
    AuthSubject,
    User,
    is_single_organization_credential,
)
from repalis.auth.scope import Scope
from repalis.exceptions import NotPermitted
from repalis.models.organization import Organization

# Not for unclaimed agents: events embed the customer they belong to.
_EventRead = Authenticator(
    required_scopes={
        Scope.events_read,
        Scope.events_write,
    },
    allowed_subjects={User, Organization},
)
EventRead = Annotated[AuthSubject[User | Organization], Depends(_EventRead)]

_EventNamesRead = Authenticator(
    required_scopes={
        Scope.events_read,
        Scope.events_write,
    },
    allowed_subjects={User, Organization, Agent},
)
EventNamesRead = Annotated[
    AuthSubject[User | Organization | Agent], Depends(_EventNamesRead)
]

_EventWrite = Authenticator(
    required_scopes={
        Scope.events_write,
    },
    allowed_subjects={User, Organization, Agent},
)
EventWrite = Annotated[AuthSubject[User | Organization | Agent], Depends(_EventWrite)]


async def _event_write_single_organization(
    auth_subject: EventWrite,
) -> AuthSubject[User | Organization | Agent]:
    if not is_single_organization_credential(auth_subject):
        raise NotPermitted(
            "Ingesting events requires an organization access token, "
            "or an OAuth token scoped to a single organization."
        )
    return auth_subject


EventWriteSingleOrganization = Annotated[
    AuthSubject[User | Organization | Agent],
    Depends(_event_write_single_organization),
]
