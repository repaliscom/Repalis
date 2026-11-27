from enum import StrEnum
from typing import Annotated

from fastapi import Depends

from repalis.kit.sorting import Sorting, SortingGetter


class WalletSortProperty(StrEnum):
    created_at = "created_at"
    balance = "balance"


ListSorting = Annotated[
    list[Sorting[WalletSortProperty]],
    Depends(SortingGetter(WalletSortProperty, ["-created_at"])),
]
