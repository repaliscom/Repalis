from pydantic import Field

from repalis.customer_meter.schemas import CustomerMeterBase
from repalis.kit.schemas import IDSchema, MultipleQueryFilter, TimestampedSchema
from repalis.kit.versioning import QuerySchema
from repalis.meter.schemas import NAME_DESCRIPTION as METER_NAME_DESCRIPTION
from repalis.meter.schemas import MeterID


class CustomerCustomerMeterMeter(IDSchema, TimestampedSchema):
    name: str = Field(description=METER_NAME_DESCRIPTION)


class CustomerCustomerMeter(CustomerMeterBase):
    meter: CustomerCustomerMeterMeter


class CustomerPortalMeterListParams(QuerySchema):
    meter_id: MultipleQueryFilter[MeterID] | None = Field(
        None, title="MeterID Filter", description="Filter by meter ID."
    )
    query: str | None = Field(None, description="Filter by meter name.")
