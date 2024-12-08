# main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar el directorio static para servir archivos estáticos como CSS, imágenes, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar Jinja2 para renderizar plantillas HTML
templates = Jinja2Templates(directory="templates")

# Ruta para la página principal (Índice)
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta para la página de Introducción
@app.get("/introduccion", response_class=HTMLResponse)
async def read_introduccion(request: Request):
    return templates.TemplateResponse("introduccion.html", {"request": request})

# Ruta para la página de Definición del Problema
@app.get("/problema", response_class=HTMLResponse)
async def read_problema(request: Request):
    return templates.TemplateResponse("problema.html", {"request": request})

# Ruta para la página de Selección y Preparación de Datos
@app.get("/preparacion", response_class=HTMLResponse)
async def read_preparacion(request: Request):
    return templates.TemplateResponse("preparacion.html", {"request": request})

# Ruta para la página de Diccionario de Datos
@app.get("/diccionario", response_class=HTMLResponse)
async def read_diccionario(request: Request):
    return templates.TemplateResponse("diccionario.html", {"request": request})

# Ruta para la página de Narración con Datos
@app.get("/graficos", response_class=HTMLResponse)
async def read_graficos(request: Request):
    return templates.TemplateResponse("graficos.html", {"request": request})

# Ruta para la página de Implementación Técnica
@app.get("/implementacion", response_class=HTMLResponse)
async def read_implementacion(request: Request):
    return templates.TemplateResponse("implementacion.html", {"request": request})

# Ruta para la página de Originalidad y Creatividad
@app.get("/creatividad", response_class=HTMLResponse)
async def read_creatividad(request: Request):
    return templates.TemplateResponse("creatividad.html", {"request": request})

# Ruta para la página de Conclusiones Generales
@app.get("/conclusiones", response_class=HTMLResponse)
async def read_conclusiones(request: Request):
    return templates.TemplateResponse("conclusiones.html", {"request": request})

# Ruta para la página de Anexo de Códigos
@app.get("/anexo", response_class=HTMLResponse)
async def read_anexo(request: Request):
    return templates.TemplateResponse("anexo.html", {"request": request})
