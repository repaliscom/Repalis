from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, Organization, User
from repalis.auth.scope import Scope

_MetricsRead = Authenticator(
    required_scopes={Scope.metrics_read},
    allowed_subjects={User, Organization},
)
MetricsRead = Annotated[AuthSubject[User | Organization], Depends(_MetricsRead)]

_MetricsWrite = Authenticator(
    required_scopes={Scope.metrics_write},
    allowed_subjects={User, Organization},
)
MetricsWrite = Annotated[AuthSubject[User | Organization], Depends(_MetricsWrite)]
