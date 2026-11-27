from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, Organization, User
from repalis.auth.scope import Scope

_SeatRead = Authenticator(
    required_scopes={
        Scope.customer_seats_read,
    },
    allowed_subjects={User, Organization},
)
SeatRead = Annotated[AuthSubject[User | Organization], Depends(_SeatRead)]

_SeatWrite = Authenticator(
    required_scopes={
        Scope.customer_seats_write,
    },
    allowed_subjects={User, Organization},
)
SeatWrite = Annotated[AuthSubject[User | Organization], Depends(_SeatWrite)]
