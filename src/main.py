from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from services import URLgenerator
from models import URLfields
from database import getLongURL, analUpdate, deleteURL

from datetime import datetime, timezone


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

@app.get("/redirect")
def redirect(shortURL: str):
    res = getLongURL(shortURL=shortURL)

    if res is None or res[1] < datetime.now(timezone.utc) :
        raise HTTPException(status_code=404, detail="Link either doesn't exist or has expired")

    analUpdate(shortURL=shortURL)
    return RedirectResponse(url=res[0], status_code=307)

@app.delete("/delete")
def deleteLink(shortURL: str):
    check = getLongURL(shortURL=shortURL)

    if check is None:
        raise HTTPException(status_code=404, detail="No matching short link found")

    deleteURL(shortURL=shortURL)
    return {"detail": "Link Deleted"}


    



