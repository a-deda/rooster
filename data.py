import pandas as pd
from domain.room import Room
from domain.timeblock import TimeBlock
from domain.student import Student
from domain.course import Course

class Data:

    def __init__(self):
        # Put csv in dataframe object
        dfStudents = pd.read_csv("files/studentenenvakken.csv", encoding="ISO-8859-1")
        dfCourses = pd.read_csv("files/courses.csv")

        students = []
        for index, row in dfStudents.iterrows():
            newStudent = Student(row[2])
            students.append(newStudent)

        self.courses = []
        for index, row in dfCourses.iterrows():
            newCourse = Course(row[0], students, row[3])
            self.courses.append(newCourse)


        # Set rooms with sizes
        room1 = Room(1, 41)
        room2 = Room(2, 22)
        room3 = Room(3, 20)
        room4 = Room(4, 56)
        room5 = Room(5, 48)
        room6 = Room(6, 117)
        room7 = Room(7, 60)
        self.rooms = [room1, room2, room3, room4, room5, room6, room7]

        # Set timeblocks
        timeblock1 = TimeBlock(1, 9)
        timeblock2 = TimeBlock(2, 11)
        timeblock3 = TimeBlock(3, 13)
        timeblock4 = TimeBlock(4, 15)
        self.timeblocks = [timeblock1, timeblock2, timeblock3, timeblock4]



    def getCourses():
        return self.courses
