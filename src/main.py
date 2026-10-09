from fastapi import FastAPI
from src.mvp import shorten

app = FastAPI(
    title="Simple URL Shortener",
    description="Don't deep it. It is literally what it says"
)

@app.post("/url-short")
def urlShort(str : s):
    shorten(s)


