"""
FastAPI pagination for DataTables

Provides a pagination class to be used with DataTables.

This is an example of the output JSON:

    {
        "data": [
            { ... },
            { ... },
            ...
        ],
        "recordsTotal": 13613,
        "length": 10,
        "start": 1,
        "draw": 1,
        "length": 10,
        "recordsFiltered": 13613,
        "success": true,
        "error": ""
    }

"""
from typing import Generic, Sequence, TypeVar

from fastapi import Query
from fastapi_pagination.bases import AbstractParams, RawParams
from fastapi_pagination.limit_offset import LimitOffsetPage as BaseLimitOffsetPage
from fastapi_pagination.limit_offset import LimitOffsetParams as BaseLimitOffsetParams

T = TypeVar("T")


class Params(BaseLimitOffsetParams, AbstractParams):
    """
    Process the parameters from the request

    - FastApi pagination requires limit and offset
    - DataTables gives start (that start with zero) and length
    """

    draw: int = 1
    start: int = Query(0, ge=0, description="Page offset")
    length: int = Query(10, ge=1, le=10, description="Page size limit")

    def to_raw_params(self) -> RawParams:
        """Define limit and offset with start and length"""
        return RawParams(
            limit=self.length,
            offset=self.start,
        )


class DataTablePage(BaseLimitOffsetPage[T], Generic[T]):
    """DataTablePage"""

    __params_type__ = Params

    data: Sequence[T]
    draw: int
    recordsTotal: int
    recordsFiltered: int
    start: int
    length: int
    limit: int
    offset: int
    success: bool = True
    error: str = ""

    class Config:
        """Set alias for DataTables"""

        allow_population_by_field_name = True
        fields = {
            "items": {"alias": "data"},
            "total": {"alias": "recordsTotal"},
            "offset": {"alias": "start"},
            "limit": {"alias": "length"},
        }

    @classmethod
    def create(
        cls,
        items: Sequence[T],
        total: int,
        params: AbstractParams,
    ) -> BaseLimitOffsetPage[T]:
        """Create"""

        # If total is zero, set error to "No se encontraron resultados"
        if total == 0:
            return cls(
                success=False,
                error="No se encontraron resultados",
                data=[],
                draw=params.draw,
                length=params.length,
                start=params.start,
                recordsTotal=total,
                recordsFiltered=total,
            )

        return cls(
            data=items,
            draw=params.draw,
            length=params.length,
            start=params.start,
            recordsTotal=total,
            recordsFiltered=total,
        )


def datatable_page_success_false(error: Exception) -> dict:
    """Return a dict with success=False and error"""
    return {
        "data": [],
        "draw": 1,
        "recordsTotal": 0,
        "start": 0,
        "length": 0,
        "recordsFiltered": 0,
        "success": False,
        "error": str(error),
    }
