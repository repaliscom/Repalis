from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, User
from repalis.auth.scope import Scope
from repalis.models.organization import Organization

_CustomerMeterRead = Authenticator(
    required_scopes={
        Scope.customer_meters_read,
    },
    allowed_subjects={User, Organization},
)

_CustomerMeterWrite = Authenticator(
    required_scopes={
        Scope.customers_write,
    },
    allowed_subjects={User, Organization},
)

CustomerMeterRead = Annotated[
    AuthSubject[User | Organization], Depends(_CustomerMeterRead)
]

CustomerMeterWrite = Annotated[
    AuthSubject[User | Organization], Depends(_CustomerMeterWrite)
]
