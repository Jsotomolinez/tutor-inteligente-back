# 🤖 Tutor Inteligente de IA para Programación

¡Bienvenido a **Tutor Inteligente**!  
Este proyecto es un asistente de inteligencia artificial diseñado para ayudarte a resolver ejercicios de programación de manera rápida y eficiente. Solo sube tu ejercicio o imagen y recibe una guía paso a paso para resolverlo.  

## 🚀 Características

- 🧑‍💻 Analiza ejercicios de programación y genera comentarios guía en Python.
- 🖼️ Soporte para imágenes de ejercicios.
- 🔒 Responde únicamente a preguntas relacionadas con programación.
- ⚡ API rápida basada en FastAPI.

## 📦 Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/jsotomolinez/llm-project-1.git
   ```
2. Instala las dependencias de producción:
   ```sh
   pip install -r requirements.txt
   ```
   Si vas a trabajar en desarrollo, instala también las dependencias adicionales:
   ```sh
   pip install -r requirements-dev.txt
   ```
3. Configura tus variables de entorno en `.env`.

## 🛠️ Uso

Inicia el servidor con:
```sh
uvicorn main:app --reload
```
Accede a la documentación en `http://localhost:8000/docs` para ver los endpoints disponibles y probar la API.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

¡Gracias por usar **Tutor Inteligente**! Esperamos que este proyecto te sea de gran ayuda en tu aprendizaje y práctica de programación.