from datetime import datetime

from pydantic import UUID4, Field

from repalis.benefit.schemas import BenefitID
from repalis.file.schemas import FileDownload
from repalis.kit.schemas import MultipleQueryFilter, Schema
from repalis.kit.versioning import QuerySchema


class DownloadableURL(Schema):
    url: str
    expires_at: datetime


class DownloadableRead(Schema):
    id: UUID4
    benefit_id: UUID4

    file: FileDownload


class CustomerPortalDownloadablesListParams(QuerySchema):
    benefit_id: MultipleQueryFilter[BenefitID] | None = Field(
        None, title="BenefitID Filter", description="Filter by benefit ID."
    )
