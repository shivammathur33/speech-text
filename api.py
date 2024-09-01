from src.entity_detect import entity_detect
from src.transcription import transcribe
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
orig_origins = [
    "http://localhost:3000",  # React app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orig_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract_entities/")
def create_item(item: dict):
    utterance=transcribe()
    address=entity_detect(utterance)
    return {"Origin": address[0],
            "Destination": address[1]}