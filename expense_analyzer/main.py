"""Server endpoint."""
import asyncio

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker

from expense_analyzer.config import app_setting
from expense_analyzer.constants import DbConstants

app = FastAPI()


@app.get("/")
async def root():
    """Example get method.

    return: example dict.
    """
    return {"message": "Hello World"}


async def run_server():
    """
    TODO: Place the code for running the server
    FIXME: api Docker files can't run the application
    :return: None
    """
    async_session = async_sessionmaker(DbConstants.ENGINE, expire_on_commit=False)
    print(async_session)

if __name__ == "__main__":
    asyncio.run(run_server())
    uvicorn.run(
        app,
        host=app_setting.host.exploded, port=app_setting.port,
    )
