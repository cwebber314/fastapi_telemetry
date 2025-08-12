"""Example FastAPI server connected to logfire

fastapi dev app/main.py
"""
from fastapi import HTTPException
import fastapi
import time
import random
import os
from sqlalchemy import create_engine, text

import logfire
logfire.configure(token=os.getenv("LOGFIRE_TOKEN"), service_name="main")
# logfire.instrument_system_metrics()

logfire.info("FastAPI server starting up")  

app = fastapi.FastAPI()

engine = create_engine("sqlite:///:memory:")
logfire.instrument_sqlalchemy(engine=engine)

create_table_sql = """
CREATE TABLE IF NOT EXISTS users (
    name VARCHAR(50) NOT NULL
);
"""

with engine.connect() as connection:
    connection.execute(text(create_table_sql))
    connection.commit()


# This shouldn't be a GET but I'm lazy for this example
@app.get("/add")
async def foobar():
    add_user_sql = """
        INSERT INTO users (name) VALUES ("John Clark")
    """
    with engine.connect() as connection:
        connection.execute(text(add_user_sql))
        connection.commit() 
    return {"message": "foo bar"}


@app.get("/throw-something")
async def throw_something():
    raise HTTPException("Ooops")


@app.get("/hello")
async def hello():
    print("hello print to STDOUT")
    return {"message": "hello world"}


@app.get("/long1")
async def hello():
    rsec = random.random() * 4
    time.sleep(rsec)
    rsec = random.random() * 2
    time.sleep(rsec)

    return {"message": "long1"}

@app.get("/long2")
async def hello():
    with logfire.span('Step 1'):
        rsec = random.random() * 4
        time.sleep(rsec)
    with logfire.span('Step 2'):
        rsec = random.random() * 2
        time.sleep(rsec)

    return {"message": "long2"}

logfire.instrument_fastapi(app, capture_headers=False)
