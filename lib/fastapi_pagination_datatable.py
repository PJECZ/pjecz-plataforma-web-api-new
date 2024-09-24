"""
FastAPI pagination for DataTables
"""

from typing import Any, Generic, Optional, Sequence, TypeVar

from fastapi import Query
from fastapi_pagination.bases import AbstractPage, AbstractParams, RawParams
from fastapi_pagination.limit_offset import LimitOffsetParams

T = TypeVar("T")


class DataTableParams(LimitOffsetParams):
    """Process the parameters from the request"""

    start: int = Query(0, ge=0, description="Page offset")
    length: int = Query(10, ge=1, le=10, description="Page size limit")

    def to_raw_params(self) -> RawParams:
        """Define limit and offset with start and length"""
        return RawParams(limit=self.length, offset=self.start)


class DataTable(AbstractPage[T], Generic[T]):
    """DataTable"""

    success: bool
    error: str

    data: Sequence[T]
    start: int
    length: int
    recordsTotal: int
    recordsFiltered: int

    __params_type__ = DataTableParams

    @classmethod
    def create(cls, items: Sequence[T], params: AbstractParams, *, total: Optional[int] = None, **kwargs: Any):
        """Create"""

        assert isinstance(params, DataTableParams)
        assert total is not None

        return cls(
            success=True,
            error="",
            data=items,
            start=params.start,
            length=params.length,
            recordsTotal=total,
            recordsFiltered=total,
        )


def custom_datatable_sucess_false(error: Exception) -> DataTable:
    """Return a CustomDataTable with success=False and error message"""

    return DataTable(
        success=False,
        error=str(error),
        data=[],
        start=0,
        length=10,
        recordsTotal=0,
        recordsFiltered=0,
    )
