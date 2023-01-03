import os

import requests
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def hello():
    return {"Hello": "World"}

@app.get("/own_secret")
def get_own_secret():
    secret_value = os.getenv("SECRET_VALUE")
    return {"Value": secret_value}

@app.get("/other_secret")
def get_other_secret():
    other_api_url = os.getenv("OTHER_API_URL")
    secret_value = requests.get(f"{other_api_url}/own_secret")
    print(secret_value.json())
    return {"Value": secret_value.json()}
