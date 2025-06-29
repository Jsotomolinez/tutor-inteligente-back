import base64
from typing import Union

# Function to encode the image
def encode_image(image: Union[str, bytes]) -> str:
    '''
    Encodes an image file (ruta o bytes) to a base64 string.
    '''
    if isinstance(image, str):
        with open(image, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    elif isinstance(image, bytes):
        return base64.b64encode(image).decode('utf-8')
    else:
        raise ValueError("El argumento debe ser una ruta de archivo o bytes.")