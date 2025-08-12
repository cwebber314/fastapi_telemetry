"""
To run without opentelemetry:

    opentelemetry-instrument python test1.py

"""
from opentelemetry import trace
import time
import random

tracer = trace.get_tracer("grafana")

@tracer.start_as_current_span("test1.throw-something")
def throw_something():
    raise Exception("Ooops")


@tracer.start_as_current_span("test1.foobar")
def foobar():
    return {"message": "foo bar"}


@tracer.start_as_current_span("test1.hello")
def hello():
    print("hello print to STDOUT")
    return {"message": "hello world"}


@tracer.start_as_current_span("test1.long1")
def long1():
    print("long1")
    with tracer.start_as_current_span("long-running-task-1"):
        rsec = random.random() * 4
        time.sleep(rsec)
    with tracer.start_as_current_span("long-running-task-2"):
        rsec = random.random() * 2
        time.sleep(rsec)

    return {"message": "long1"}

long1()
foobar()
hello()