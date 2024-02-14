from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/operaciones_cadena/{cadena}")
def operaciones_cadena(cadena: str):
    contador = 0 
    for letra in cadena:
        if letra in "aeiou":
            contador += 1
    longitud_cad = len(cadena)
    return{"La palabra introducida es: ": cadena, "La longitud de la palabra introducida es: ": longitud_cad, "Nº de letras: ": len(cadena)}