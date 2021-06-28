from fastapi import FastAPI, HTTPException
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


@app.post('/', status_code=201)
async def add_course(payload: Course):
    course = payload.dict()
    fake_course_db.append(course)
    return {'id': len(fake_course_db) - 1}


@app.put('/{id')
async def update_course(id: int, payload: Course):
    course = payload.dict()
    course_length = len(fake_course_db)
    if 0 <= id <= course_length:
        fake_course_db[id] = course
        return None
    raise HTTPException(status_code=404, detail='Course with given id is not found')
