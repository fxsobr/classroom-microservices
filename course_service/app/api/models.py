from typing import List
from pydantic import BaseModel


class Course(BaseModel):
    name: str
    description: str
    students: List[str]
