from fastapi import FastAPI

from course_service.app.api.courses import courses
from course_service.app.api.db import metadata, engine, database

metadata.create_all(engine)

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(courses)
