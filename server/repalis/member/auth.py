from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, User
from repalis.auth.scope import Scope
from repalis.models.organization import Organization

_MemberRead = Authenticator(
    required_scopes={
        Scope.members_read,
        Scope.members_write,
    },
    allowed_subjects={User, Organization},
)
MemberRead = Annotated[AuthSubject[User | Organization], Depends(_MemberRead)]

_MemberWrite = Authenticator(
    required_scopes={
        Scope.members_write,
    },
    allowed_subjects={User, Organization},
)
MemberWrite = Annotated[AuthSubject[User | Organization], Depends(_MemberWrite)]
