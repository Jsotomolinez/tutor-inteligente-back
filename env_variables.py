import os

# Cargar dotenv solo en desarrollo
if os.getenv("ENV", "development") == "development":
    try:
        from dotenv import load_dotenv
        load_dotenv(".env")
    except ImportError:
        pass  # No hay problema si dotenv no está instalado en producción


# Obtener variables de entorno críticas
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FRONT_END_URL = os.getenv("FRONT_END_URL")


# Validar que las variables críticas estén definidas
if not GEMINI_API_KEY:
    raise RuntimeError("La variable de entorno GEMINI_API_KEY es obligatoria.")
if not FRONT_END_URL:
    raise RuntimeError("La variable de entorno FRONT_END_URL es obligatoria.")