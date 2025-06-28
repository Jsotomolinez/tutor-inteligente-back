from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from routers.gemini import gemini_router


app = FastAPI(
    title="Tutor inteligente",
    description="Asistente de IA para la resolución de ejercicios de programación",
    version="Building...",
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit/",
    },
)

# Limitar las llamadas a la API a 10 por minuto
# # limiter = Limiter(key_func=get_remote_address)
# # app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)




app.include_router(gemini_router)


origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)