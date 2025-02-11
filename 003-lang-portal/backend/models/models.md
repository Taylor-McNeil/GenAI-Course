# Database Relationships

This document explains the relationships between the tables in the Lang Portal database, including one-to-many and many-to-many relationships with examples.

## List of Tables and Their Purpose

| Table Name | Purpose |
| --| -- |
| words | Stores Spanish vocabulary words and English translations.
| groups| Represents collections of words, such as categories (e.g., Animals 🐇, clothing 👖).|
| word_groups | A **join table** that links words to groups. | 
| study_sessions | Tracks study sessions, including which words were reviewed and the group studied.
| word_review_items| Stores individual word review attempts, including correctness.|
| study_activities| Represents different types of study activities available to users

## 1. Words & Word Reviews (One-to-Many)
### Description:

- Each word can have multiple review attempts.

- Each review belongs to only one word.

### Tables & Relationships:

| Words Table | WordReviewItem Table|
|---|---|
|id = 1 , spanish_word = "el gato", english_word = "the cat" | id = 1, word_id = 1, study_session_id = 1, correct = false,  created_at = 2025-02-31|
|id = 1 , spanish_word = "el gato", english_word = "the cat" | id = 1, word_id = 1, study_session_id = 1, correct = true, created_at = 2025-02-31|

## 2. Study Sessions & Word Reviews (One-to-Many)

### Description: 
- Each study session can have multiple word reviews.

- Each word review belongs to one study session.

### Tables & Relationships:

| StudySession Table | WordReviewItem Table |
|--|--|
|id = 1 (Session #1), group_id = 1, study_activity_id=1, created_at = 2025-02-31 | id = 1, word_id = 1, study_session_id = 1, correct = false,  created_at = 2025-02-31|
|id = 1 (Session #1), group_id = 1, study_activity_id=1, created_at = 2025-02-31 | id = 2, word_id = 2, study_session_id = 1, correct = false, created_at = 2025-02-31 |
|id = 2 (Session #2), group_id = 1, study_activity_id=1, created_at = 2025-02-31 | id = 3, word_id = 1, study_session_id = 2, correct = true, created_at = 2025-02-31 |

## 3. Study Activities & Study Sessions (One-to-Many)
### Description
- Each study session is linked to **one study activity.

- Each study activity can be used in multiple study sessions.


### Tables & Relationships:
| StudyActivity Table | StudySession Table|
|--|--|
| id = 1, name = Typing Tutor, url = {} | id = 1 , group_id = 1, study_activity_id = 1, created_at = 2025-02-31 |
| id = 2, name = Flashcards, url = {} | id = 2, group_id = 1, study_activity_id = 2,  created_at = 2025-02-31 |
| id = 2 name = Flashcards, url = {} | id = 3, group_id =2,  study_activity_id = 2,  created_at = 2025-02-31|


## 4. Study Sessions & Groups (One-to-Many)
### Description
- Each study session belongs to one group.

- Each group can have multiple study sessions.
### Tables & Relationships:
| Group Table | StudySession Table|
|--|--|
| id = 1, group_name = Animals 🐇, word_count = 10 | id = 1, group_id = 1, study_activity_id = 1, created_at = 2025-02-31 |
| id = 2, group_name = Clothing 👖, word_count = 3 | id = 2, group_id = 2, study_activity_id = 1, created_at = 2025-02-31  |
| id = 1, group_name = Animals 🐇, word_count = 10 | id = 3, group_id = 1, study_activity_id = 1, created_at = 2025-02-31 |


## 5. Words & Groups (Many-to-Many)
### Description
- A word can belong to multiple groups.

- A group can contain multiple words.

- This requires a **join table** (word_groups).



### Tables & Relationships:
| Words Table| WordGroup Table| GroupsTable|
|--|--|--|
| id = 1, spanish_word = "el gato", english_word = "the cat" | word_id = 1, group_id = 1| id = 1, group_name = Animals , word_count = 10|
|id = 2, spanish_word = "el perro", english_word = "the dog"| word_id = 2, group_id = 1 |  id = 1, group_name = Animals , word_count = 10|

---
## 🎯 Final Summary
| Relationship Type | Description|
|--|--|
| One-to-Many |A Word has many WordReviewItems. |
| One-to-Many | A StudySession has many WordReviewItems. |
| One-to-Many| A StudyActivity has many StudySessions. |
| One-to-Many| A StudySession belongs to one Group. |
| Many-to-Many| A Word belongs to multiple Groups, and a Group contains multiple Words. |