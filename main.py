from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def read_root():
    return  {"Hello": "World","Status":"I an ready for Spring Recruitment"}

@app.get("/add")
def add_numbers(a:int,b:int):
    return {"result":a+b}