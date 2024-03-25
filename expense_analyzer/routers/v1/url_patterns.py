from fastapi import APIRouter

from expense_analyzer.constants import (
    RouterPrefixConstants,
    RouterTagConstants
)
from expense_analyzer.routers.v1.currency import currency_router

v1_router = APIRouter(
    tags=RouterTagConstants.V1_TAGS,
    prefix=RouterPrefixConstants.V1,
)


v1_router.include_router(router=currency_router)
