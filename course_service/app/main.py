from fastapi import FastAPI

from course_service.app.api.courses import courses

app = FastAPI()

app.include_router(courses)