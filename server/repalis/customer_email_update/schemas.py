from repalis.kit.email import EmailStrDNS
from repalis.kit.schemas import Schema


class CustomerEmailUpdateRequest(Schema):
    email: EmailStrDNS


class CustomerEmailUpdateVerifyRequest(Schema):
    token: str


class CustomerEmailUpdateVerifyResponse(Schema):
    token: str
