from fastapi import APIRouter

from expense_analyzer.constants import (RouterPrefixConstants,
                                        RouterTagConstants)
from expense_analyzer.routers.type_annotations import (ItemIdDependency,
                                                       PaginationDependency)

currency_router = APIRouter(
    tags=RouterTagConstants.CURRENCY_TAGS,
    prefix=RouterPrefixConstants.CURRENCY,
)

PATH_TO_CRUD_WITHOUT_ITEM_ID = ''
PATH_TO_CRUD_WITH_ITEM_ID = '/{item_id}'


@currency_router.get(path=PATH_TO_CRUD_WITHOUT_ITEM_ID)
async def read_all_items(pagination: PaginationDependency):
    return {'message': await pagination}


@currency_router.get(path=PATH_TO_CRUD_WITH_ITEM_ID)
async def read_item(item_id: ItemIdDependency):
    return {'message': await item_id}


@currency_router.patch(path=PATH_TO_CRUD_WITH_ITEM_ID)
async def partial_update_item(item_id: ItemIdDependency):
    return {'message': await item_id}


@currency_router.post(path=PATH_TO_CRUD_WITHOUT_ITEM_ID)
async def create_item():
    return {'message': 'successful'}


@currency_router.delete(path=PATH_TO_CRUD_WITH_ITEM_ID)
async def remove_item(item_id: ItemIdDependency):
    return {'message': await item_id}
