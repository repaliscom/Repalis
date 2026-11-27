from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, Organization, User
from repalis.auth.scope import Scope

LicenseKeysRead = Annotated[
    AuthSubject[User | Organization],
    Depends(
        Authenticator(
            required_scopes={
                Scope.license_keys_read,
                Scope.license_keys_write,
            },
            allowed_subjects={User, Organization},
        )
    ),
]

LicenseKeysWrite = Annotated[
    AuthSubject[User | Organization],
    Depends(
        Authenticator(
            required_scopes={
                Scope.license_keys_write,
            },
            allowed_subjects={User, Organization},
        )
    ),
]
