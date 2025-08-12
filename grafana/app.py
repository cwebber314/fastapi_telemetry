"""
See:

https://grafana.com/blog/2024/02/20/how-to-instrument-your-python-application-using-opentelemetry/

To start:

flask run -p 8080
http://localhost:8080/rolldice

"""
from random import randint
from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/rolldice")
def roll_dice():
    player = request.args.get('player', default = None, type = str)
    result = str(roll())
    if player:
        logger.warn("%s is rolling the dice: %s", player, result)
    else:
        logger.warn("Anonymous player is rolling the dice: %s", result)
    return result

def roll():
    return randint(1, 6)