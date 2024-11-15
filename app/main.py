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
    uvicorn.run(app, host="0.0.0.0", port=8000)
