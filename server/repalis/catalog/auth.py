from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import Agent, AuthSubject, Organization, User
from repalis.auth.scope import Scope

_CatalogRead = Authenticator(
    required_scopes={Scope.products_read, Scope.products_write},
    allowed_subjects={User, Organization, Agent},
)
CatalogRead = Annotated[AuthSubject[User | Organization | Agent], Depends(_CatalogRead)]

_CatalogWrite = Authenticator(
    required_scopes={Scope.products_write},
    allowed_subjects={User, Organization, Agent},
)
CatalogWrite = Annotated[
    AuthSubject[User | Organization | Agent], Depends(_CatalogWrite)
]
