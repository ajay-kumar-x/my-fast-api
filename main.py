from fastapi import FastAPI
import models
import dbHelper as dbh

app=FastAPI()

@app.get('/')
async def home():
    return "Home"


# Endpoint to create a new Student
@app.post("/students/", response_model=models.Student)
async def add_student(student: models.Student):
    await dbh.add_student(student)
    return student

@app.get("/students/{roll_no}", response_model=models.Student)
async def get_student_by_roll_no(roll_no:int):
    student=await dbh.get_student_by_roll_no(roll_no)
    return student
