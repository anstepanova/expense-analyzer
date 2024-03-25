from typing import Any

from expense_analyzer.constants import PathParametersDefaultValues


async def write_all_parameters_to_dict(**kwargs: Any) -> dict[str, Any]:
    return kwargs


async def pagination_dependency(
        skip: int = PathParametersDefaultValues.SKIP_ITEMS_FOR_PAGINATION,
        limit: int = PathParametersDefaultValues.LIMIT_ITEMS_FOR_PAGINATION,
):
    return write_all_parameters_to_dict(skip=skip, limit=limit)


async def item_id_dependency(item_id: int):
    return write_all_parameters_to_dict(item_id=item_id)
