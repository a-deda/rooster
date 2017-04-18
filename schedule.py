from data import Data
from domain.uniclass import UniClass
import random

class Schedule:

    def __init__(self, data):
        self.data = data
        self.uniclasses = [None]*len(self.data.courses)

    def initialize(self):
        for i, course in enumerate(self.data.courses):
            newUniClass = UniClass(course)
            newUniClass.setRoom(random.choice(self.data.rooms))
            newUniClass.setTimeBlock(random.choice(self.data.timeblocks))
            self.uniclasses[i] = newUniClass
        return self

    def calculateFitness(self):
        conflicts = 0
        for index, uniclass in enumerate(self.uniclasses):
            if uniclass.room.max < len(uniclass.course.students):
                conflicts += 1
            for uniclass2 in self.uniclasses[index+1:]:
                if uniclass.timeBlock.id == uniclass2.timeBlock.id:
                    if uniclass.room.id == uniclass2.room.id:
                        conflicts += 1
                    students1 = [x.id for x in uniclass.course.students]
                    students2 = [x.id for x in uniclass2.course.students]
                    if len(set(students1) & set(students2)) > 0:
                        conflicts += 1
        return float(1)/(conflicts + 1)

    def crossOver(self, partner):
        child = Schedule(self.data)
        for x in range(len(self.uniclasses)):
            if random.uniform(0,1) < 0.1:
                newUniClass = UniClass(self.uniclasses[x].course)
                newUniClass.setRoom(random.choice(self.data.rooms))
                newUniClass.setTimeBlock(random.choice(self.data.timeblocks))
                child.uniclasses[x] = newUniClass
            elif random.uniform(0, 1) > 0.5:
                child.uniclasses[x] = self.uniclasses[x]
            else:
                child.uniclasses[x] = partner.uniclasses[x]
        return child



    def printClasses(self):
        string = ""
        for uniclass in self.uniclasses:
            string += uniclass.toString()+"\n"
        return string
