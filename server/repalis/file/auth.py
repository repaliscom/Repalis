from typing import Annotated

from fastapi.params import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import Agent, AuthSubject, Organization, User
from repalis.auth.scope import Scope

_FileRead = Authenticator(
    required_scopes={
        Scope.files_write,
        Scope.files_read,
    },
    allowed_subjects={User, Organization, Agent},
)
FileRead = Annotated[AuthSubject[User | Organization | Agent], Depends(_FileRead)]

_FileWrite = Authenticator(
    required_scopes={
        Scope.files_write,
    },
    allowed_subjects={User, Organization, Agent},
)
FileWrite = Annotated[AuthSubject[User | Organization | Agent], Depends(_FileWrite)]
