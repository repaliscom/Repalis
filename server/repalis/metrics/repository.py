from uuid import UUID

from sqlalchemy import Select

from repalis.authz.types import AccessibleOrganizationID
from repalis.kit.repository import RepositoryBase, RepositoryIDMixin
from repalis.models import MetricDashboard


class MetricDashboardRepository(
    RepositoryBase[MetricDashboard], RepositoryIDMixin[MetricDashboard, UUID]
):
    model = MetricDashboard

    def get_statement_by_org_ids(
        self, org_ids: set[AccessibleOrganizationID]
    ) -> Select[MetricDashboard]:
        statement = self.get_base_statement()
        statement = statement.where(MetricDashboard.organization_id.in_(org_ids))
        return statement
