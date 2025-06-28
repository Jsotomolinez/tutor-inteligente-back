from fastapi import APIRouter, HTTPException, UploadFile, File, Form

from helpers.images import encode_image

from openai import OpenAI

import os
from dotenv import load_dotenv

gemini_router = APIRouter(prefix="/gemini", tags=["gemini"])

load_dotenv(".secrets")
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY environment variable is not set.")


client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


@gemini_router.post("/chat")
async def get_gemini_response(prompt: str):
    try:
        response = client.chat.completions.create(
            model="gemini-1.5-flash",
            messages=[
                {"role": "user", "content": prompt}
            ],
            
            max_tokens=500,
            temperature=0.1
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@gemini_router.post("/chat/image")
async def get_gemini_response_from_image(
    file: UploadFile = File(...),
    isTextFile: str = Form(...),
    isFunction: str = Form(...)
):
    try:
        # Leer el archivo recibido
        contents = await file.read()
        with open("temp_image", "wb") as f:
            f.write(contents)
        base64_image = encode_image("temp_image")
        os.remove("temp_image")

        is_text_file = isTextFile.lower() == 'true'
        is_function = isFunction.lower() == 'true'

        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f'''
Quiero que analices la imagen que te he enviado y escribas una serie de comentarios de python de una línea que sirvan como guia para poder resolver el ejercicio.
En la primera línea indica el nombre del ejercicio, evita decir "proyecto #" solo di el nombre del proyecto.
Evita el uso de comillas triples.
No coloques el mensaje inicial de "Claro, aquí tienes un guia para resolver el ejercicio".
No coloques el mensaje final de "¿Hay algo más en lo que te pueda ayudar?"
No envuelas la respuesta en comillas triples.
Si la pregunta que se te hace no es de progrmación, responde con "Lo siento pero me diseñaron para responder preguntas de programación".
{"El problema requiere que menejes archivos de texto." if is_text_file else "El problema no requiere que manejes archivos de texto."}
{"El problema requiere que manejes funciones." if is_function else "El problema no requiere que manejes funciones, no definas ninguna."}
Si la imagen que se te ha enviado no es un ejercicio de programación, responde con "Lo siento pero me diseñaron para responder preguntas de programación".
'''
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url":  f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
        )
        return response.choices[0].message.content.replace('\n', '<br />').replace("'''", '').removeprefix('"').removesuffix('"')

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
