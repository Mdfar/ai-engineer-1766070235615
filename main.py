from fastapi import FastAPI, HTTPException from pydantic import BaseModel from ai_engine import AIEngine from schema import DocumentAnalysis

app = FastAPI(title="AI Document Intelligence API") ai = AIEngine()

class DocumentRequest(BaseModel): text: str

@app.get("/") def read_root(): return {"status": "online", "feature": "Document Intelligence"}

@app.post("/analyze", response_model=DocumentAnalysis) async def analyze_text(request: DocumentRequest): if not request.text.strip(): raise HTTPException(status_code=400, detail="Text content cannot be empty")

try:
    # End-to-end extraction and validation
    result = await ai.analyze_document(request.text)
    return result
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))


if name == "main": import uvicorn uvicorn.run(app, host="0.0.0.0", port=8000)