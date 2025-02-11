from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.models.schemas.word import WordCreate, WordResponse
from backend.crud.word import *
from backend.core.database import get_db

router = APIRouter()

# Get all words (GET)
@router.get("/words/", response_model=List[WordResponse])
def fetch_words(db:Session = Depends(get_db)):
    words = get_all_words(db)
    return [WordResponse.from_orm(word) for word in words]