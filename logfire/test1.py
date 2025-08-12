"""Example of using logfire in a generic python script
"""
from fastapi import FastAPI
import os
import time
import random
import logfire

app = FastAPI()

logfire.configure(token=os.getenv("LOGFIRE_TOKEN"), service_name="test1")
# logfire.configure()  
logfire.info('Hello, {name}!', name='world')  

def throw_something():
    raise Exception("Ooops")
    return {"message": "foo bar"}


def foobar():
    return {"message": "foo bar"}


def hello():
    print("hello print to STDOUT")
    return {"message": "hello world"}


def long1():
    print("long1")
    rsec = random.random() * 4
    time.sleep(rsec)
    rsec = random.random() * 2
    time.sleep(rsec)
    return {"message": "long1"}

# throw_something()
long1()
# long1()
foobar()
hello()