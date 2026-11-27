from pydantic import Field

from repalis.benefit.schemas import BenefitID
from repalis.kit.versioning import QuerySchema


class CustomerPortalLicenseKeyListParams(QuerySchema):
    benefit_id: BenefitID | None = Field(
        None, description="Filter by a specific benefit"
    )
