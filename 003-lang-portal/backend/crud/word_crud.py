from sqlalchemy.orm import Session
from models.models import Word
from schemas.word_schema import WordCreate, WordResponse
from typing import List, Optional

# Create a Word

def create_word(db:Session,word_data: WordCreate) -> WordResponse:
    word = Word(**word_data.dict())
    db.add(word)
    db.commit()
    db.refresh(word)
    return word # Returns ORM object, automatically converted to WordResponse

def get_all_words(db: Session) -> List[Word]:
    words = db.query(Word).all()
    return [WordResponse.model_validate(word) for word in words]  # ✅ Convert each ORM object individually

def get_word_by_id(db:Session, word_id:int) ->Optional[WordResponse]:
    word = db.query(Word).filter(Word.id == word_id).first()
    return WordResponse.model_validate(word) if word else None