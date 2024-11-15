import os
import uvicorn
from fastapi import FastAPI
import logging
import sys

from common import set_logger

set_logger.set_logger()

logger = logging.getLogger(__name__)


app = FastAPI()


@app.get("/")
def read_root():
    logger.debug("Hello World")
    return {"Hello": "World"}


if __name__ == "__main__":
    logger.info("++++++++Start server")
    HTTP_HOST = os.getenv("HTTP_HOST", "localhost")
    HTTP_PORT = int(os.getenv("HTTP_PORT", 8000))
    uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT)
