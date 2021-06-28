from fastapi import FastAPI

from api.courses import courses

app = FastAPI()

app.include_router(courses)