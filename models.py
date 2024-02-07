from pydantic import BaseModel

class Student(BaseModel):
    roll_no:int
    name:str
    class_name:int

class Marks(BaseModel):
    roll_no:int
    english:int
    hindi:int
    science:int
    math:int

# CREATE TABLE STUDENT (
#     roll_no INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     class_name INT NOT NULL
# );
