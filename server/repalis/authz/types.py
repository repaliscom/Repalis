from collections.abc import Awaitable, Callable
from typing import Literal, NewType
from uuid import UUID

from repalis.auth.models import Agent, AuthSubject, Organization, User
from repalis.models import Organization as OrganizationModel
from repalis.postgres import AsyncReadSession

# A UUID that has been verified as accessible by the current auth subject.
# Only get_accessible_org_ids should produce these values.
AccessibleOrganizationID = NewType("AccessibleOrganizationID", UUID)

# Policy functions return True if allowed, or a denial reason string if denied.
PolicyResult = Literal[True] | str

PolicyFn = Callable[
    [AsyncReadSession, AuthSubject[User | Organization | Agent], OrganizationModel],
    Awaitable[PolicyResult],
]
