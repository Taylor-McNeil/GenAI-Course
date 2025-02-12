import csv
from backend.core.database import SessionLocal
from backend.models.models import Group, Word, WordGroup

db = SessionLocal()

#Load the words from the CSV file

def load_words():
    with open("backend/models/seedData/words.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word = Word(spanish_word=row["spanish_word"], english_word=row["english_word"])
            existing_word = db.query(Word).filter(Word.spanish_word == word.spanish_word).first()

            if not existing_word:   
                db.add(word)
                print(f"Added word: {word.spanish_word} - {word.english_word}")
            else:
                print(f"Word already present: {existing_word.spanish_word} - {existing_word.english_word}")    
    db.commit()

#Load the groups from the CSV file

def load_groups():
    with open("backend/models/seedData/groups.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            group = Group(group_name=row["group_name"])
            existing_group = db.query(Group).filter(Group.group_name == group.group_name).first()
            if not existing_group:
                db.add(group)
                print(f"Added group: {group.group_name}")
            else:
                print(f"Group already present: {existing_group.group_name}")    
    db.commit()

    
#Load the word groups from the CSV file

def load_word_groups():    
    with open("backend/models/seedData/word_groups.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word_group = WordGroup(word_id=row["word_id"], group_id=row["group_id"])
            existing_entry = db.query(WordGroup).filter_by(word_id=row["word_id"], group_id=row["group_id"]).first()

            if not existing_entry:
                 db.add(word_group)
                 group = db.query(Group).filter(Group.id == word_group.group_id).first()
                 if group:
                    group.word_count += 1
                    db.add(group)
                    print(f"Added relationship between word_id: {word_group.word_id} and group_id: {word_group.group_id}")
            else:
                print(f"Relationship already present")     
            
           
            
    db.commit()

if __name__ == "__main__":
    load_words()
    load_groups()
    load_word_groups()
    db.close()
    print("Seed data loaded successfully!")    