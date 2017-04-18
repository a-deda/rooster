from domain.room import Room
from domain.timeblock import TimeBlock
from domain.student import Student
from domain.course import Course

class Data:

    def __init__(self):
        room1 = Room(1, 1)
        room2 = Room(2, 2)
        room3 = Room(3, 3)
        self.rooms = [room1, room2, room3]
        timeblock1 = TimeBlock(1, 9)
        timeblock2 = TimeBlock(2, 11)
        timeblock3 = TimeBlock(3, 13)
        timeblock4 = TimeBlock(4, 15)
        self.timeblocks = [timeblock1, timeblock2, timeblock3, timeblock4]
        student1 = Student(1)
        student2 = Student(2)
        student3 = Student(3)
        self.students = [student1, student2, student3]
        course1 = Course("frans", [student1, student2], 2)
        course2 = Course("latijn", [student1], 1)
        course3 = Course("wiskunde", [student1, student3], 2)
        course4 = Course("natuurkunde", [student3], 1)
        course5 = Course("spaans", [student1, student2, student3], 3)
        self.courses = [course1, course2, course3, course4, course5]

    def getCourses():
        return self.courses
