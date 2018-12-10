from cls_pkg.person import PERSON


class STUDENT(PERSON):
    def __init__(self, id):
        self.id = id


    def print_id(self):
        print("Student id: {}".format(self.id))