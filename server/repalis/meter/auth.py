from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import Agent, AuthSubject, User
from repalis.auth.scope import Scope
from repalis.models.organization import Organization

_MeterRead = Authenticator(
    required_scopes={
        Scope.meters_read,
        Scope.meters_write,
    },
    allowed_subjects={User, Organization, Agent},
)
MeterRead = Annotated[AuthSubject[User | Organization | Agent], Depends(_MeterRead)]

_MeterWrite = Authenticator(
    required_scopes={
        Scope.meters_write,
    },
    allowed_subjects={User, Organization, Agent},
)
MeterWrite = Annotated[AuthSubject[User | Organization | Agent], Depends(_MeterWrite)]
