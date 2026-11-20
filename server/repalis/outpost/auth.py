from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, Organization
from repalis.auth.scope import Scope

OutpostWrite = Annotated[
    AuthSubject[Organization],
    Depends(
        Authenticator(
            required_scopes={Scope.events_write}, allowed_subjects={Organization}
        )
    ),
]
