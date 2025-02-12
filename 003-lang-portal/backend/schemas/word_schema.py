from pydantic import BaseModel, ConfigDict
from typing import Dict, Optional

#Base Scheme (Shared fields)
class WordBase(BaseModel):
    spanish_word: str
    english_word: str

class WordCreate(WordBase):
    pass #Inherits all fields from WordBase, thus we can use pass here

class WordResponse(WordBase):
    id: int #We are sending the id back to the user and the rest of the information, so we cannot use pass here
    model_config = ConfigDict(from_attributes=True)  # ✅ Needed for ORM conversion