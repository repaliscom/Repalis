import pytest
from pytest_mock import MockerFixture

from repalis.invoice.seller import (
    get_repalis_additional_info,
    get_repalis_vat_label,
    get_repalis_vat_number,
)
from repalis.kit.address import Address, CountryAlpha2


def _address(country: str, state: str | None = None) -> Address:
    return Address(country=CountryAlpha2(country), state=state)


VAT_NUMBERS = {
    "FR": "EU372061545",
    "DE": "EU372061545",
    "GB": "GB458254961",
    "CA": "720474766 RT9999",
    "NZ": "148-410-224",
}


@pytest.fixture(autouse=True)
def configured_vat_numbers(mocker: MockerFixture) -> None:
    mocker.patch("repalis.invoice.seller.settings.INVOICES_VAT_NUMBERS", VAT_NUMBERS)
    mocker.patch(
        "repalis.invoice.seller.settings.INVOICES_ADDITIONAL_INFO",
        "[support@repalis.com](mailto:support@repalis.com)",
    )


class TestGetRepalisVatNumber:
    def test_none_country(self) -> None:
        assert get_repalis_vat_number(None) is None

    def test_known_country(self) -> None:
        assert get_repalis_vat_number("FR") == "EU372061545"
        assert get_repalis_vat_number("DE") == "EU372061545"
        assert get_repalis_vat_number("GB") == "GB458254961"

    def test_unknown_country(self) -> None:
        assert get_repalis_vat_number("US") is None
        assert get_repalis_vat_number("JP") is None


class TestGetRepalisVatLabel:
    def test_none_address(self) -> None:
        assert get_repalis_vat_label(None) == "VAT"

    def test_default_label(self) -> None:
        assert get_repalis_vat_label(_address("FR")) == "VAT"
        assert get_repalis_vat_label(_address("GB")) == "VAT"
        assert get_repalis_vat_label(_address("US")) == "VAT"

    def test_canada(self) -> None:
        assert get_repalis_vat_label(_address("CA")) == "GST/HST"

    def test_chile(self) -> None:
        assert get_repalis_vat_label(_address("CL")) == "RUT"

    def test_kenya(self) -> None:
        assert get_repalis_vat_label(_address("KE")) == "PIN"

    def test_korea(self) -> None:
        assert get_repalis_vat_label(_address("KR")) == "BRN"

    def test_new_zealand(self) -> None:
        assert get_repalis_vat_label(_address("NZ")) == "GST"


class TestGetRepalisAdditionalInfo:
    def test_mapped_country(self) -> None:
        info = get_repalis_additional_info(_address("FR"))
        assert (
            info
            == "[support@repalis.com](mailto:support@repalis.com)\nVAT: EU372061545"
        )

    def test_uk(self) -> None:
        info = get_repalis_additional_info(_address("GB"))
        assert (
            info
            == "[support@repalis.com](mailto:support@repalis.com)\nVAT: GB458254961"
        )

    def test_canada_uses_gst_hst_label(self) -> None:
        info = get_repalis_additional_info(_address("CA"))
        assert info == (
            "[support@repalis.com](mailto:support@repalis.com)\nGST/HST: 720474766 RT9999"
        )

    def test_new_zealand_uses_gst_label(self) -> None:
        info = get_repalis_additional_info(_address("NZ"))
        assert info == (
            "[support@repalis.com](mailto:support@repalis.com)\nGST: 148-410-224"
        )

    def test_unmapped_country(self) -> None:
        info = get_repalis_additional_info(_address("US"))
        assert info == "[support@repalis.com](mailto:support@repalis.com)"

    def test_none_address(self) -> None:
        info = get_repalis_additional_info(None)
        assert info == "[support@repalis.com](mailto:support@repalis.com)"

    def test_empty_settings_returns_none(self, mocker: MockerFixture) -> None:
        mocker.patch("repalis.invoice.seller.settings.INVOICES_ADDITIONAL_INFO", None)
        mocker.patch("repalis.invoice.seller.settings.INVOICES_VAT_NUMBERS", {})
        assert get_repalis_additional_info(_address("FR")) is None
        assert get_repalis_additional_info(None) is None

    def test_only_vat_when_no_additional_info(self, mocker: MockerFixture) -> None:
        mocker.patch("repalis.invoice.seller.settings.INVOICES_ADDITIONAL_INFO", None)
        assert get_repalis_additional_info(_address("FR")) == "VAT: EU372061545"

    def test_only_additional_info_when_no_vat(self, mocker: MockerFixture) -> None:
        mocker.patch("repalis.invoice.seller.settings.INVOICES_VAT_NUMBERS", {})
        assert get_repalis_additional_info(_address("FR")) == (
            "[support@repalis.com](mailto:support@repalis.com)"
        )
