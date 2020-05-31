from typing import Optional, List, Dict, Union

from fastapi import FastAPI

from api.config import DEBUG, VERSION, APP_NAME


def get_application() -> FastAPI:
    application = FastAPI(
        title=APP_NAME,
        debug=DEBUG,
        version=VERSION
    )

    return application


app = get_application()
