from fastapi import FastAPI
from pydantic import BaseModel
import telegramify_markdown

app = FastAPI()

class Item(BaseModel):
    text: str

@app.post("/markdownify")
def convert_markdown(item: Item):
    try:
        converted = telegramify_markdown.markdownify(
            item.text,
            max_line_length=None,
            normalize_whitespace=False
        )
        return {"result": converted}
    except Exception as e:
        return {"error": str(e)}
