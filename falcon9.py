from functools import reduce
from pprint import pprint
from uuid import uuid4

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    instance = Falcon9()
    pprint(instance)
    return '{}'.format(instance)
# from models.falcon9 import falcon9

class Dragon:
    def __init__(self):
        self.uuid = uuid4()

class Merlin1D:
    def __init__(self):
        self.thrustLBF = 205000
        self.weightKG = 470
        self.uuid = uuid4()


class Merlin1DVacuum:
    def __init__(self):
        self.thrustLBF = 210000
        self.weightKG = 470
        self.uuid = uuid4()

class CompositeFairing:
    def __init__(self, payload=[]):
        self.payload = payload
        self.uuid = uuid4()

class Engine:
    def __init__(self, type):
        if type == 'Merlin1D':
            instance = Merlin1D()
        elif type == 'Merlin1DVacuum':
            instance = Merlin1DVacuum()
        self.thrustLBF = instance.thrustLBF
        self.weightKG = instance.weightKG
        self.uuid = instance.weightKG


class Interstage:
    def __init__(self):
        self.engines = []
        self.uuid = uuid4()


class SecondStage:
    def __init__(self):
        self.engines = [
            Engine('Merlin1DVacuum')
        ]
        self.uuid = uuid4()


class FirstStage:
    def __init__(self):
        self.engines = [
            Engine('Merlin1D'),
            Engine('Merlin1D'),
            Engine('Merlin1D'),
            Engine('Merlin1D'),
            Engine('Merlin1D'),
            Engine('Merlin1D'),
            Engine('Merlin1D'),
            Engine('Merlin1D'),
            Engine('Merlin1D'),
        ]
        self.uuid = uuid4()


class Falcon9:
    def __init__(self):
        self.stages = [
            Dragon(),
            CompositeFairing(),
            SecondStage(),
            Interstage(),
            FirstStage(),
        ]
        self.uuid = uuid4()
        def returnEngines (x):
            return (x.engines)
        self.engines = map(returnEngines, self.stages)
    def __str__(self):
        return str(self.uuid)

    def __repr__(self):
        return "%s: %s" % (self.__class__.__name__, str(self))
