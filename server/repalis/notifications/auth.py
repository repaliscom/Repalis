from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, User
from repalis.auth.scope import Scope

_NotificationsRead = Authenticator(
    required_scopes={
        Scope.notifications_read,
    },
    allowed_subjects={User},
)
NotificationsRead = Annotated[AuthSubject[User], Depends(_NotificationsRead)]

_NotificationsWrite = Authenticator(
    required_scopes={
        Scope.notifications_write,
    },
    allowed_subjects={User},
)
NotificationsWrite = Annotated[AuthSubject[User], Depends(_NotificationsWrite)]
