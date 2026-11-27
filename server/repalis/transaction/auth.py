from typing import Annotated

from fastapi import Depends

from repalis.auth.dependencies import Authenticator
from repalis.auth.models import AuthSubject, User
from repalis.auth.scope import Scope

_TransactionsRead = Authenticator(
    required_scopes={
        Scope.transactions_read,
    },
    allowed_subjects={User},
)
TransactionsRead = Annotated[AuthSubject[User], Depends(_TransactionsRead)]

_TransactionsWrite = Authenticator(
    required_scopes={
        Scope.transactions_write,
    },
    allowed_subjects={User},
)
TransactionsWrite = Annotated[AuthSubject[User], Depends(_TransactionsWrite)]
