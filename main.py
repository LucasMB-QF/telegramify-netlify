from fastapi import FastAPI, Form
from pydantic import BaseModel
from telegramify_markdown import markdownify

app = FastAPI()

# Endpoint normal (JSON)
class TextPayload(BaseModel):
    text: str

@app.post("/markdownify")
async def convert_json(payload: TextPayload):
    return markdownify(payload.text)

# NUEVO ENDPOINT – acepta texto RAW sin JSON
@app.post("/raw-markdownify")
async def convert_raw(text: str = Form(...)):
    return markdownify(text)
