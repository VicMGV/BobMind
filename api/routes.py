from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List
from api.models import AnalysisResponse, SummaryResponse, HypothesisResponse
from bob.analyzer import analyze_document, summarize_document, generate_hypothesis
from documents.loader import load_document
from documents.processor import clean_text
from profiles import PROFILES

router = APIRouter()

@router.get("/profiles")
def list_profiles():
    return {"profiles": list(PROFILES.keys())}

@router.get("/health")
def health():
    return {"status": "ok", "service": "BobMind"}

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze(
    profile: str = Form(...),
    question: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        file_bytes = await file.read()
        filename = file.filename or "document.txt"
        document_text = load_document(filename, file_bytes)
        document_text = clean_text(document_text)
        result = analyze_document(profile, document_text, question)
        return AnalysisResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/summarize", response_model=SummaryResponse)
async def summarize(
    profile: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        file_bytes = await file.read()
        filename = file.filename or "document.txt"
        document_text = load_document(filename, file_bytes)
        document_text = clean_text(document_text)
        result = summarize_document(profile, document_text)
        return SummaryResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/hypothesis", response_model=HypothesisResponse)
async def hypothesis(
    profile: str = Form(...),
    files: List[UploadFile] = File(...)
):
    try:
        documents = []
        for f in files:
            file_bytes = await f.read()
            filename = f.filename or "document.txt"
            document_text = load_document(filename, file_bytes)
            document_text = clean_text(document_text)
            documents.append(document_text)
        
        result = generate_hypothesis(profile, documents)
        return HypothesisResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))