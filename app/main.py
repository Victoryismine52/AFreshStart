from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import data

app = FastAPI(title="afreshstart")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data.router)


@app.get("/")
def read_root():
    return {"message": "afreshstart API"}
