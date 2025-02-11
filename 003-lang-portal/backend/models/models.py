from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from backend.core.database import Base
from datetime import datetime

# Table: words (Vocabulary Table)
class Word(Base):
    __tablename__ = "words"

    id = Column(Integer,primary_key=True,index=True)
    spanish_word = Column(String, nullable=False)
    english_word = Column(String, nullable=False)

    # One word can be apart of many word reviews
    reviews = relationship("WordReviewItem", back_populates="word")

    # Many-to-Many Relationship with Groups
    groups = relationship("Group", secondary="word_groups", back_populates="words")

# Table: groups (Word Groups Table)
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String, nullable=False)
    word_count = Column(Integer, default=0) #Tracks the number of words in the group    

    # Many-to-Many Relationship with Words
    words = relationship("Word", secondary="word_groups", back_populates="groups")
    study_sessions = relationship("StudySession", back_populates="group")  # ✅ Links sessions to group


# Table: word_groups (Many-to-Many Relationship Between Words & Groups)
class WordGroup(Base):
    __tablename__= "word_groups"
    word_id = Column(Integer, ForeignKey("words.id"), primary_key=True) 
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)  

# Table: study_activities (Different Study Types)
class StudyActivity(Base):
    __tablename__ = "study_activities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False) # url to the study activity

    study_sessions = relationship("StudySession", back_populates="study_activity")  # ✅ Links sessions to study activity

# Table: study_sessions (Tracks Study Sessions)
class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    study_activity_id = Column(Integer, ForeignKey("study_activities.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    reviews = relationship("WordReviewItem", back_populates="study_session")
    group = relationship("Group", back_populates="study_sessions")  # ✅ Allows fetching group easily
    study_activity = relationship("StudyActivity", back_populates="study_sessions")  # ✅ Fetch study activity easily

class WordReviewItem(Base):
    __tablename__ = "word_review_items"

    id = Column(Integer, primary_key=True, index=True)
    word_id = Column(Integer, ForeignKey("words.id"))
    study_session_id = Column(Integer, ForeignKey("study_sessions.id"))
    correct = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    word = relationship("Word", back_populates="reviews")
    study_session = relationship("StudySession", back_populates="reviews")