"""
FastAPI Pagination Custom Page
"""

from typing import Any, Generic, Optional, Sequence, TypeVar

from fastapi import Query
from fastapi_pagination.bases import AbstractPage, AbstractParams, RawParams
from fastapi_pagination.limit_offset import LimitOffsetParams

T = TypeVar("T")


class CustomPageParams(LimitOffsetParams):
    """Process the parameters from the request"""

    limit: int = Query(10, ge=1, le=50, description="Query limit")
    offset: int = Query(0, ge=0, description="Query offset")

    def to_raw_params(self) -> RawParams:
        """Define limit and offset"""
        return RawParams(limit=self.limit, offset=self.offset)


class CustomPage(AbstractPage[T], Generic[T]):
    """Custom Page"""

    success: bool
    message: str

    total: int
    limit: int
    offset: int
    items: Sequence[T]

    __params_type__ = CustomPageParams

    @classmethod
    def create(cls, items: Sequence[T], params: AbstractParams, *, total: Optional[int] = None, **kwargs: Any):
        """Create"""

        assert isinstance(params, CustomPageParams)
        assert total is not None

        return cls(
            success=True,
            message="Success",
            total=total,
            limit=params.limit,
            offset=params.offset,
            items=items,
        )


def custom_page_success_false(error: Exception) -> CustomPage:
    """Return a CustomPage with success=False and message=error"""

    return CustomPage(
        success=False,
        message=str(error),
        total=0,
        limit=10,
        offset=0,
        items=[],
    )
