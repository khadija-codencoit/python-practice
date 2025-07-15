import json
from pathlib import Path

movies = [
    {"id":1 , "Title":"Titanic" },
    {"id":2 , "Title":"Kindergaden" }

]

data = json.dumps(movies) #str output
print(data)

Path("movies.json").write_text(data) #write json file

#Write them into a students.json file.

students = [
    {"roll": 101, "name": "Ayesha", "grade": "A"},
    {"roll": 102, "name": "Rafi", "grade": "B+"}
]

student_info = json.dumps(students)
print(student_info)
Path("student.json").write_text(student_info)