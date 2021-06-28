from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ARRAY

DATABASE_URL = 'postgresql://course_user:course_password@localhost/course_db'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

courses = Table(
    'courses',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('description', String(250)),
    Column('students', ARRAY(String))
)

database = Database(DATABASE_URL)