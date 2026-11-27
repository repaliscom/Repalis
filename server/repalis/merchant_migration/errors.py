from repalis.exceptions import RepalisError


class MerchantMigrationError(RepalisError):
    """Base for everything this module raises, so a caller can catch the whole
    feature in one clause."""
