from fastapi import HTTPException, APIRouter
from typing import List

from course_service.app.api.models import Course

courses = APIRouter()


@courses.get('/', response_model=List[CourseOut])
async def index():
    return await db_manager.get_all_courses()


@courses.post('/', status_code=201)
async def add_course(payload: CourseIn):
    course_id = await db_manager.add_course(payload)
    response = {
        'id': course_id,
        **payload.dict()
    }
    return response


@courses.put('/{id')
async def update_course(id: int, payload: CourseIn):
    course = await db_manager.get_movie(id)
    if not course:
        raise HTTPException(status_code=404, detail='Course not found')

    update_data = payload.dict(exclude_unset=True)
    course_in_db = CourseIn(**course)

    updated_course = course_in_db.copy(update=update_data)

    return await db_manager.update_course(id, updated_course)



@courses.delete('/{id}')
async def delete_course(id: int):
    courses_length = len(fake_course_db)
    if 0 <= id <= courses_length:
        del fake_course_db[id]
        return None
    raise HTTPException(status_code=404, detail='Course with given id is not found')
