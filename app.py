from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from translator import Translator

# Initialize FastAPI app
app = FastAPI()

# Correct static file path (relative to the location of app.py)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2 templates and translator
templates = Jinja2Templates(directory="templates")
translator = Translator()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Serve the HTML template
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/translate/")
async def translate_text(text: str = Form(...)):
    # Process the translation
    translated_text = translator.translate(text)
    return {"original": text, "translated": translated_text}
