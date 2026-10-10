from fastapi import FastAPI, HTTPException
from services import URLgenerator
from models import URLfields


app = FastAPI(
    title="Simple URL Shortener",
    description="Don't deep it. It is literally what it says"
)

@app.post("/url-short")
def urlShort(fields: URLfields):
    res = URLgenerator(longURL=fields.longUrl, customDomain=fields.customDomain, alias=fields.alias)

    if res is None:
        raise HTTPException(status_code=409, detail="Alias already taken")

    return res





