"""Example fastapi service with zero-code instrumentation.

See: https://opentelemetry.io/docs/zero-code/

To run with telemetry:

    opentelemetry-instrument --traces_exporter console,otlp \
                            --metrics_exporter console \
                            --service_name zero \
                            fastapi run server_programmtic.py

I cna't get this to work quite right. Honeycomb complains that there are no traces
"""
from fastapi import HTTPException
import fastapi
import time
import random

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.trace import get_tracer_provider, set_tracer_provider

set_tracer_provider(TracerProvider())
get_tracer_provider().add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter())
)

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

instrumentor = FastAPIInstrumentor()
instrumentor.instrument_app(app)