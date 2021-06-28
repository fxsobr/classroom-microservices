from fastapi import HTTPException, APIRouter
from typing import List

from course_service.app.api.models import Course

courses = APIRouter()

fake_course_db = [
    {
        'name': 'Python',
        'description': 'Introduction to Programming',
        'students': ['Marcelo Ceolin', 'Jean C']
    }
]


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
    courses_length = len(fake_course_db)
    if 0 <= id <= courses_length:
        fake_course_db[id] = course
        return None
    raise HTTPException(status_code=404, detail='Course with given id is not found')


@app.delete('/{id}')
async def delete_course(id: int):
    courses_length = len(fake_course_db)
    if 0 <= id <= courses_length:
        del fake_course_db[id]
        return None
    raise HTTPException(status_code=404, detail='Course with given id is not found')
