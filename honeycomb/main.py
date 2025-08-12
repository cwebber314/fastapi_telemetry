"""
To run without opentelemetry:

    fastapi dev main.py

To run with telemetry:

    opentelemetry-instrument fastapi dev main.py

"""
from fastapi import HTTPException
import fastapi
from opentelemetry import trace
import time
import random

app = fastapi.FastAPI()
tracer = trace.get_tracer("sandbox.fastapi")

@tracer.start_as_current_span("fastapi.foobar")
@app.get("/foobar")
async def foobar():
    return {"message": "foo bar"}


@tracer.start_as_current_span("fastapi.throw-something")
@app.get("/throw-something")
async def throw_something():
    raise HTTPException("Ooops")


@tracer.start_as_current_span("fastapi.hello")
@app.get("/hello")
async def hello():
    print("hello print to STDOUT")
    return {"message": "hello world"}


@tracer.start_as_current_span("fastapi.long1")
@app.get("/long1")
async def hello():
    with tracer.start_as_current_span("long-running-task-1"):
        rsec = random.random() * 4
        time.sleep(rsec)
    with tracer.start_as_current_span("long-running-task-2"):
        rsec = random.random() * 2
        time.sleep(rsec)

    return {"message": "long1"}
