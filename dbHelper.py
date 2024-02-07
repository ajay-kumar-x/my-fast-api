from fastapi import HTTPException
import mysql.connector
import models

# MySQL connection parameters
# config = {
#     "user": "root",
#     "password": "rootdevaws",
#     "host": "student-db.cxccmq2ecku9.ap-south-1.rds.amazonaws.com",
#     "port":3306,
#     "database": "student-db"
# }
config = {
    "user": "admin",
    "password": "adminaws",
    "host": "testing.cxccmq2ecku9.ap-south-1.rds.amazonaws.com",
    "port":3306,
    "database":"testing"
}


# MySQL connection
connection = mysql.connector.connect(**config)



# Function to check if table exists
def table_exists(table_name):
    cursor = connection.cursor()
    create_database_query = "CREATE DATABASE IF NOT EXISTS testing"
    cursor.execute(create_database_query)
    cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return cursor.fetchone() is not None

# Function to create the table if it doesn't exist
def create_table_if_not_exists():
    if not table_exists("STUDENT"):
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE STUDENT (
                roll_no INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                class_name INT
            )
            """
        )
        connection.commit()

async def add_student(student: models.Student):
     create_table_if_not_exists()  # Check and create table if necessary
     cursor =connection.cursor()
     cursor.execute(
        "INSERT INTO STUDENT (roll_no,name, class_name) VALUES (%s, %s, %s)",
        (student.roll_no, student.name, student.class_name)
        )
     connection.commit()

async def get_student_by_roll_no(roll_no: int):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM STUDENT WHERE roll_no = %s",
        (roll_no,)
    )
    student = cursor.fetchone()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# config = {
#     "user": "root",
#     "password": "root",
#     "host": "127.0.0.1",
#     "port":3306,
#     "database": "testing"
# }