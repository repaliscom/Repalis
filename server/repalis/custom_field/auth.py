from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, User
from repalis.auth.scope import Scope
from repalis.models.organization import Organization

_CustomFieldRead = Authenticator(
    required_scopes={
        Scope.custom_fields_read,
        Scope.custom_fields_write,
    },
    allowed_subjects={User, Organization},
)
CustomFieldRead = Annotated[AuthSubject[User | Organization], Depends(_CustomFieldRead)]

_CustomFieldWrite = Authenticator(
    required_scopes={
        Scope.custom_fields_write,
    },
    allowed_subjects={User, Organization},
)
CustomFieldWrite = Annotated[
    AuthSubject[User | Organization], Depends(_CustomFieldWrite)
]
