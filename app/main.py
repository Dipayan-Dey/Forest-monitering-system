from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Allowed frontend
    allow_credentials=True,
    allow_methods=["*"],            # GET, POST, PUT, DELETE
    allow_headers=["*"],          
)


@app.get("/")
def home():
    return {"message": " Server is Running"}