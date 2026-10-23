from fastapi import FastAPI
from schemas import TodoCreate
from database import engine, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/todos", status_code=201)
def create_todo(body: TodoCreate):
    return {"message": "successfully created"}



