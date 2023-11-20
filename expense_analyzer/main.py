"""Server endpoint."""
import uvicorn
from config import app_setting
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Example get method.

    return: example dict.
    """
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=app_setting.host.exploded, port=app_setting.port,
    )
