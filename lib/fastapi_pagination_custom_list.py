"""
FastAPI Pagination Custom List
"""

from typing import Generic, Optional, Sequence, TypeVar

from fastapi import Query
from fastapi_pagination.bases import AbstractPage, AbstractParams
from fastapi_pagination.default import Params
from typing_extensions import Self

T = TypeVar("T")


class CustomListParams(Params):
    """Process the parameters from the request"""

    size: int = Query(200, ge=1, le=400, description="Page size")


class CustomList(AbstractPage[T], Generic[T]):
    """Custom List"""

    success: bool
    message: str

    total: int
    size: int
    items: Sequence[T] = []

    __params_type__ = CustomListParams

    @classmethod
    def create(cls, items: Sequence[T], params: AbstractParams, *, total: Optional[int] = None) -> Self:
        """Create"""

        assert isinstance(params, CustomListParams)
        assert total is not None

        return cls(
            success=True,
            message="Success",
            total=total,
            size=params.size,
            items=items,
        )


def custom_list_success_false(error: Exception) -> CustomList:
    """Return a CustomList with success=False and message=error"""

    return CustomList(
        success=False,
        message=str(error),
        total=0,
        size=0,
        items=[],
    )
