from typing import Annotated

from fastapi import Depends

from expense_analyzer.routers.dependencies import (
    item_id_dependency,
    pagination_dependency
)

PaginationDependency = Annotated[dict, Depends(pagination_dependency)]
ItemIdDependency = Annotated[dict, Depends(item_id_dependency)]
