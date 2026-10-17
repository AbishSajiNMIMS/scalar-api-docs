# API Documentation with Scalar — Cat Facts API

Small FastAPI wrapper around https://catfact.ninja whose OpenAPI spec is
generated automatically and rendered with Scalar.

## Run
    python -m venv venv
    venv\Scripts\activate          (Mac/Linux: source venv/bin/activate)
    pip install -r requirements.txt
    uvicorn main:app --reload

## Open
- http://127.0.0.1:8000/scalar        Scalar docs + built-in API client
- http://127.0.0.1:8000/openapi.json  auto-generated OpenAPI spec
- http://127.0.0.1:8000/docs          FastAPI's default Swagger UI (for comparison)

## Files
- main.py           the API (3 endpoints) and the /scalar route
- openapi.json      saved copy of the generated spec
- requirements.txt  Python packages
- screenshots/      proof of each step
- Project_Report.docx  procedure, explanations and research answers