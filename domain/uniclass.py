class UniClass:

    def __init__(self, course):
        self.course = course
        self.activity = None
        self.room = None
        self.timeBlock = None
        self.students = []

    def setActivity(self, activity):
        self.activity = activity

    def setRoom(self, room):
        self.room = room

    def setTimeBlock(self, timeBlock):
        self.timeBlock = timeBlock

    def setStudents(self, students):
        self.students = students

    def toString(self):
        return str(self.timeBlock.time) + "-"+str(self.timeBlock.time+2)+", " + str(self.course.name) + ", " +  str(self.room.id)
