from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from .predictor import get_toxicity_score

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
def root_form():
    html_content = """
    <html>
        <head>
            <title>Анализ текста на токсичность</title>
            <style>
                .container {
                    font-family: Arial;
                    max-width: 600px;
                    margin: auto;
                    padding-top: 40px;
                }
                .progress {
                    background-color: #eee;
                    border-radius: 5px;
                    overflow: hidden;
                    margin-top: 10px;
                }
                .bar {
                    height: 25px;
                    text-align: center;
                    color: white;
                    line-height: 25px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Анализ текста на токсичность</h2>
                <form action="/" method="post">
                    <textarea name="text" rows="4" cols="60" placeholder="Введите текст на русском...">Ты ужасный человек!</textarea><br><br>
                    <input type="submit" value="Проверить токсичность">
                </form>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/", response_class=HTMLResponse)
def predict_form(text: str = Form(...)):
    score = get_toxicity_score(text)
    percent = int(score * 100)
    color = "#28a745" if percent < 30 else ("#ffc107" if percent < 70 else "#dc3545")
    html_content = f"""
    <html>
        <head>
            <title>Результат классификации</title>
            <style>
                .container {{
                    font-family: Arial;
                    max-width: 600px;
                    margin: auto;
                    padding-top: 40px;
                }}
                .progress {{
                    background-color: #eee;
                    border-radius: 5px;
                    overflow: hidden;
                    margin-top: 10px;
                }}
                .bar {{
                    height: 25px;
                    width: {percent}%;
                    background-color: {color};
                    text-align: center;
                    color: white;
                    line-height: 25px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Результат классификации</h2>
                <p><strong>Текст:</strong> {text}</p>
                <p><strong>Оценка токсичности:</strong> {score:.4f}</p>
                <div class="progress">
                    <div class="bar">{percent}%</div>
                </div>
                <br>
                <a href="/">← Назад</a>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/predict")
def predict(input_data: TextInput):
    try:
        score = get_toxicity_score(input_data.text)
        return {"toxicity_score": score}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))