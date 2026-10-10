from pydantic import BaseModel
from typing import Optional

class URLfields(BaseModel):
    longUrl : str
    alias : Optional[str] = None
    customDomain : Optional[str] = None