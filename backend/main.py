from fastapi import FastAPI
from analyzer import analyze_traffic
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (important for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Network Analyzer Running"}

@app.get("/data")
def get_data():
    return analyze_traffic()