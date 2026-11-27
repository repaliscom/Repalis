from pydantic import UUID4, Field

from repalis.kit.schemas import Schema
from repalis.kit.versioning import QuerySchema
from repalis.notification_recipient.schemas import NotificationRecipientPlatform
from repalis.notifications.notification import Notification


class NotificationsList(Schema):
    notifications: list[Notification]
    last_read_notification_id: UUID4 | None


class NotificationsMarkRead(Schema):
    notification_id: UUID4


class NotificationsListParams(QuerySchema):
    expo_push_token: str | None = Field(None, description="Filter by Expo push token.")
    platform: NotificationRecipientPlatform | None = Field(
        None, description="Filter by platform."
    )
