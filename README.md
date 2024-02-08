# Chatbot con PDF

Este proyecto consiste en un chatbot capaz de interactuar con documentos en formato PDF. Utiliza Streamlit para la interfaz de usuario y diversas herramientas de procesamiento de lenguaje natural (NLP) para realizar búsquedas de similitud y responder preguntas sobre el contenido del PDF.

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalado Python, así como las siguientes bibliotecas:

- Streamlit
- PyPDF2
- NLTK
- Langchain

Puedes instalar estas dependencias utilizando pip:

```
pip install streamlit PyPDF2 nltk langchain
```

Además, necesitarás una clave de API de OpenAI para acceder a los servicios de procesamiento de lenguaje natural. Puedes obtener una clave de API registrándote en [OpenAI](https://openai.com/).

## Configuración

Antes de ejecutar la aplicación, asegúrate de configurar tu clave de API de OpenAI en el archivo `.env` o directamente en el código, asignándola a la variable `OPENAI_API_KEY`.

## Uso

Para ejecutar la aplicación, simplemente ejecuta el siguiente comando en tu terminal:

```
streamlit run nombre_del_archivo.py
```

Una vez ejecutada la aplicación, podrás cargar un archivo PDF desde la barra lateral. Una vez cargado, podrás enviar consultas al chatbot utilizando el cuadro de texto provisto. El chatbot procesará tus consultas, buscará similitudes en el contenido del PDF y te responderá con respuestas relevantes.

## Contribuciones

Siéntete libre de contribuir a este proyecto enviando sugerencias, informes de errores o mejoras de código a través de problemas y solicitudes de extracción en GitHub.

¡Disfruta interactuando con el chatbot!

---

Recuerda reemplazar `app.py` con el nombre real de tu archivo de código fuente.
