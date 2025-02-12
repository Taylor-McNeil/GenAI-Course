from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.word_schema import WordCreate, WordResponse
from crud.word_crud import *
from core.database import get_db

router = APIRouter()

# Get all words (GET)
@router.get("/words/", response_model=List[WordResponse])
def fetch_words(db:Session = Depends(get_db)):
    words = get_all_words(db)
    return [WordResponse.from_orm(word) for word in words]

@router.get("/words/{word_id}", response_model=WordResponse)
def fetch_word(word_id:int, db:Session = Depends(get_db)):
    word = get_word_by_id(db,word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")
    return WordResponse.from_orm(word)    