from repalis.auth.routing import DocumentedAuthSubjectAPIRoute
from repalis.kit.routing import (
    IncludedInSchemaAPIRoute,
    PaginationAPIRoute,
    SpeakeasyGroupAPIRoute,
    SpeakeasyIgnoreAPIRoute,
    SpeakeasyNameOverrideAPIRoute,
    SpeakeasyPaginationAPIRoute,
    ToolAPIRoute,
    TransactionalAPIRoute,
    get_api_router_class,
)
from repalis.kit.versioning import VersionedAPIRoute


class APIRoute(
    VersionedAPIRoute,
    TransactionalAPIRoute,
    IncludedInSchemaAPIRoute,
    ToolAPIRoute,
    DocumentedAuthSubjectAPIRoute,
    PaginationAPIRoute,
    SpeakeasyIgnoreAPIRoute,
    SpeakeasyNameOverrideAPIRoute,
    SpeakeasyGroupAPIRoute,
    SpeakeasyPaginationAPIRoute,
):
    pass


APIRouter = get_api_router_class(APIRoute)

__all__ = ["APIRouter"]
