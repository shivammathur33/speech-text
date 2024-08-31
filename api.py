from src.entity_detect import entity_detect
from src.transcription import transcribe
from fastapi import FastAPI
app = FastAPI()

@app.post("/extract_entities/")
def create_item(item: dict):
    utterance=transcribe()
    address=entity_detect(utterance)
    return {"Origin": address[0],
            "Destination": address[1]}