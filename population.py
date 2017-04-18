from schedule import Schedule
from data import Data
from random import randint

class Population:

    def __init__(self, size, data):
        self.schedules = [Schedule(data).initialize() for x in range(size)]
        self.matingPool = []

    def generateMatingPool(self):
        fitness = [x.calculateFitness() for x in self.schedules]
        percentage = [x/sum(fitness) for x in fitness]
        for i, item in enumerate(percentage):
            for i2 in range(int(item*10000)):
                self.matingPool.append(self.schedules[i])
        return self

    def generate(self):
        for x in range(len(self.schedules)):
            a = randint(0,len(self.matingPool))
            b = randint(0,len(self.matingPool))
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            child = partnerA.crossOver(partnerB)
            self.schedules[x] = child
        return self



data = Data()
population = Population(10, data)
print sum([x.calculateFitness() for x in population.schedules])
for x in range(1000):
    population.generateMatingPool()
    population = population.generate()
    print sum([x.calculateFitness() for x in population.schedules])
