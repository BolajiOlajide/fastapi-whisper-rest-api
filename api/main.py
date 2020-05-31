from typing import Optional, List, Dict, Union

from fastapi import FastAPI

from api.config import Config


def get_application() -> FastAPI:
    application = FastAPI(title="Whisper-API", debug=Config.DEBUG, version=Config.VERSION)

    return application


app = get_application()
