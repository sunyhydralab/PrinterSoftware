"""
Will create dummy printer objects with filaments, and dummy job queues, randomly, but using a seeding method so we can
get the same random results everytime for quick verification.
"""

import random as r
from Filament import Filament

# from Job import Job
import JobQueue
import Printer
import PriorityTable


def main():
    r.seed(10)
    filaments = createFilaments(10)
    jobs = createJobs(25)


def createFilaments(num, maxAmount=50, colors=["red", "blue"]):
    """
    Create 'num' random filament objects and return them as a list

    maxAmount is the max amount of filament a class will be randomly filled with
    """
    out = []

    for _ in range(num):
        color = r.choice(colors)
        out.append(Filament(color, maxAmount))

    return out


def createJobs(num, colors=["red", "blue"]):
    out = []

    for i in range(num):
        out.append(DummyJob(i, r.randint(2, 30), r.choice(colors)))

    return out


class DummyJob:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color


main()
