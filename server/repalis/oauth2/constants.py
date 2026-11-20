from repalis.config import settings

from .sub_type import SubType

CLIENT_ID_PREFIX = "repalis_ci_"
CLIENT_SECRET_PREFIX = "repalis_cs_"
CLIENT_REGISTRATION_TOKEN_PREFIX = "repalis_crt_"
AUTHORIZATION_CODE_PREFIX = "repalis_ac_"
ACCESS_TOKEN_PREFIX: dict[SubType, str] = {
    SubType.user: "repalis_at_u_",
    SubType.organization: "repalis_at_o_",
    SubType.agent: "repalis_at_a_",
}
# Agents get no refresh tokens: they trade their identity assertion instead.
REFRESH_TOKEN_PREFIX: dict[SubType, str] = {
    SubType.user: "repalis_rt_u_",
    SubType.organization: "repalis_rt_o_",
}

CLAIM_GRANT_TYPE = "urn:workos:agent-auth:grant-type:claim"
CLAIM_POLL_INTERVAL = 5

ISSUER = settings.BASE_URL
SERVICE_DOCUMENTATION = "https://repalis.com/docs"
SUBJECT_TYPES_SUPPORTED = ["public"]
ID_TOKEN_SIGNING_ALG = "RS256"
ID_TOKEN_SIGNING_ALG_VALUES_SUPPORTED = [ID_TOKEN_SIGNING_ALG]
ID_TOKEN_EXPIRES_IN = 3600
CLAIMS_SUPPORTED = ["sub", "name", "email", "email_verified"]


def is_registration_token_prefix(value: str) -> bool:
    return value.startswith(CLIENT_REGISTRATION_TOKEN_PREFIX)


def is_access_token_prefix(value: str) -> bool:
    return any(value.startswith(p) for p in ACCESS_TOKEN_PREFIX.values())
