from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

fake_course_db = [
    {
        'name': 'Python',
        'description': 'Introduction to Programming',
        'students': ['Marcelo Ceolin', 'Jean C']
    }
]


class Course(BaseModel):
    name: str
    description: str
    students: List[str]


@app.get('/', response_model=List[Course])
async def index():
    return fake_course_db
