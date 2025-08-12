"""Example fastapi service with zero-code instrumentation.

See: https://opentelemetry.io/docs/zero-code/

To run with telemetry:

    opentelemetry-instrument --traces_exporter console,otlp \
                            --metrics_exporter console \
                            --service_name zero \
                            fastapi run server_automatic.py

I cna't get this to work quite right. Honeycomb complains that there are no traces
"""
from fastapi import HTTPException
import fastapi
import time
import random

app = fastapi.FastAPI()

@app.get("/foobar")
async def foobar():
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

