from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from slowapi.errors import RateLimitExceeded
from env_variables import FRONT_END_URL
from routers.gemini import gemini_router



# Inicialzar de la app
app = FastAPI(
    title="Tutor inteligente",
    description="Asistente de IA para la resolución de ejercicios de programación",
    version="Building...",
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit/",
    },
)




#Enrutadores
app.include_router(gemini_router)


# Origenes para CORS
origins = [
    FRONT_END_URL,
]


# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["multipart/form-data"],
)