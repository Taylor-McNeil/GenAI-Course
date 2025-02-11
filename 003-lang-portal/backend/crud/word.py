from sqlalchemy.orm import Session
from backend.models.models import Word
from backend.models.schemas.word import WordCreate, WordResponse
from typing import List, Optional

# Create a Word

def create_word(db:Session,word_data: WordCreate) -> WordResponse:
    word = Word(**word_data.dict())
    db.add(word)
    db.commit()
    db.refresh(word)
    return word # Returns ORM object, automatically converted to WordResponse

def get_all_words(db: Session) -> List[Word]:
    return db.query(Word).all()