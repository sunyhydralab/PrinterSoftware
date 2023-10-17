"""
Will create dummy printer objects with filaments, and dummy job queues, randomly, but using a seeding method so we can
get the same random results everytime for quick verification.
"""
import random as r
from Classes.Filament import Filament

# from Job import Job
from Classes.JobQueue import JobQueue

# from Classes.Printer import Printer
from Classes.PriorityTable import PriorityTable


def main():
    r.seed(10)
    filaments = createFilaments(2)
    jobs = createJobs(5)
    queues = createQueues([1, 3, 5])

    print(filaments)
    print(jobs)
    print(queues)


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


def createQueues(prioritys):
    out = []

    id = 0
    for item in prioritys:
        out.append(JobQueue(id, item))
        id += 1

    return out


class DummyJob:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def __repr__(self):
        return f"(n: {self.name}, s: {self.size}, c: {self.color})"


main()
