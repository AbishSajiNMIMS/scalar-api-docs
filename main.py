from fastapi import FastAPI, Query
from pydantic import BaseModel
import httpx
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Cat Facts API",
    version="1.0.0",
    description="A small API that wraps https://catfact.ninja, used to demonstrate "
                "automatic OpenAPI generation and Scalar documentation.",
)

CATFACT = "https://catfact.ninja"

# ---- Data models (define what each response looks like) -------------------
class Fact(BaseModel):
    fact: str
    length: int

class Breed(BaseModel):
    breed: str
    country: str
    origin: str
    coat: str
    pattern: str

# ---- Endpoints ------------------------------------------------------------
@app.get("/fact", response_model=Fact, tags=["Facts"], summary="Get a random cat fact")
def random_fact(max_length: int | None = Query(None, description="Only return facts up to this many characters")):
    """Fetch one random cat fact from catfact.ninja."""
    params = {"max_length": max_length} if max_length else {}
    return httpx.get(f"{CATFACT}/fact", params=params, timeout=10).json()

@app.get("/facts", response_model=list[Fact], tags=["Facts"], summary="Get several cat facts")
def many_facts(limit: int = Query(5, ge=1, le=50, description="How many facts to return (1–50)")):
    """Fetch a page of cat facts from catfact.ninja."""
    return httpx.get(f"{CATFACT}/facts", params={"limit": limit}, timeout=10).json()["data"]

@app.get("/breeds", response_model=list[Breed], tags=["Breeds"], summary="List cat breeds")
def breeds(limit: int = Query(5, ge=1, le=50, description="How many breeds to return (1–50)")):
    """Fetch a page of cat breeds from catfact.ninja."""
    return httpx.get(f"{CATFACT}/breeds", params={"limit": limit}, timeout=10).json()["data"]
# ---- Scalar documentation page --------------------------------------------
@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return HTMLResponse("""
    <!doctype html>
    <html>
        <head><title>Cat Facts API – Scalar Docs</title></head>
        <body>
        <div id="app"></div>
        <script src="https://cdn.jsdelivr.net/npm/@scalar/api-reference"></script>
        <script>
            Scalar.createApiReference('#app', { url: '/openapi.json' })
        </script>
        </body>
    </html>
""")