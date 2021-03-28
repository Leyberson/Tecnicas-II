from fastapi import FastAPI
import json

app = FastAPI()


@app.get('/')
def get_root():
    return "Bem-vindo ao Leybank"


@app.get("/db")
def get_db():
    return json.load(open('backend/db/db.json'))
