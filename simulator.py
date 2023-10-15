"""
Will create dummy printer objects with filaments, and dummy job queues, randomly, but using a seeding method so we can
get the same random results everytime for quick verification.
"""

import random as r
from Filament import Filament
from Job import Job
import JobQueue
import Printer
import PriorityTable


def main():
    r.seed(10)


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


def createJobs(num):
    pass


main()
