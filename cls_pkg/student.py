from cls_pkg.person import PERSON


class STUDENT(PERSON):
    def __init__(self, id, name):
        super(STUDENT, self).__init__(name)
        self.id = id
        self.name = name

    def print_id(self):
        print("Student id: {}".format(self.id))

    def attend_college(self):
        print("Student id: {} has attended".format(self.id))

    def sit_exams(self):
        print("Student id: {} has at exams".format(self.id))
