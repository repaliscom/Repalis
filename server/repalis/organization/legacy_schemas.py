from pydantic import MISSING, Field

from repalis.kit.versioning import Omissible

from . import schemas
from .schemas import OrganizationDetails


class OrganizationCreate(schemas.OrganizationCreate):
    details: OrganizationDetails | None = Field(
        None,
        description="Additional, private, business details Repalis needs about active organizations for compliance (KYC).",
    )


class OrganizationUpdate(schemas.OrganizationUpdate):
    details: Omissible[OrganizationDetails] = Field(
        MISSING,
        description="Additional, private, business details Repalis needs about active organizations for compliance (KYC).",
    )
