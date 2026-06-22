from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Aula",
    description="Aula FastAPI",  # noqa: F821
    summary="API desenvolvida durante a aula de Construção de APIs para IA",
    version="0.1",
    terms_of_service="http://example.com/terms/",
    contact={
    "name": "Marco Antonio S. Silva",
    "url": "http://github.com/marcoassilva70/",
    "email": "marcoantoniodossantossilva70@gmail.com",
    },
    license_info={
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

class Numeros(BaseModel):
    numero1: int
    numero2: int

class Resultado(BaseModel):
    resultado: int

@app.get("/teste")
def hello_world():
    return {"mensagem": "Hello World"}

# Passando o número 1 e 2 na URL
@app.get("/soma/{numero1}/{numero2}")
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}

# Passando o número 1 e 2 no corpo da requisição
@app.post("/soma_formato2")
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}

@app.post("/soma_formato3")
def soma_formato3(numeros: Numeros) -> Resultado:
    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}