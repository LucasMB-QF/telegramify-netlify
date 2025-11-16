from fastapi import FastAPI, Body
import telegramify_markdown

app = FastAPI()

# 1) Markdown normal → Telegram MarkdownV2
@app.post("/markdownify")
def convert_markdown(text: str = Body(..., embed=True)):
    converted = telegramify_markdown.markdownify(text)
    return {"result": converted}

# 2) Telegramify → divide texto largo + renderiza
@app.post("/telegramify")
def convert_telegramify(text: str = Body(..., embed=True)):
    converted = telegramify_markdown.telegramify(text)
    return {"result": converted}

# 3) Standardize → corrige MarkdownV2 mal escrito
@app.post("/standardize")
def convert_standardize(text: str = Body(..., embed=True)):
    converted = telegramify_markdown.standardize(text)
    return {"result": converted}
