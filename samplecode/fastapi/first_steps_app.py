# uvx --with 'fastapi[standard]' fastapi dev first_steps_app.py
# ref: https://fastapi.tiangolo.com/tutorial/first-steps/
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


"""
% curl http://127.0.0.1:8000
{"message":"Hello World"}
"""
