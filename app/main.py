from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from app import servicios

app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


class RespuestaRequest(BaseModel):
    id: int
    opcion: int = Field(ge=0, le=3)


@app.get("/")
def pagina_principal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


@app.get("/api/preguntas")
def obtener_preguntas():
    return servicios.listar_preguntas()


@app.post("/api/responder")
def responder(respuesta: RespuestaRequest):
    indice_correcto = servicios.obtener_respuesta_correcta(respuesta.id)
    if indice_correcto is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")

    return {
        "correcta": respuesta.opcion == indice_correcto,
        "respuesta_correcta": indice_correcto,
    }
