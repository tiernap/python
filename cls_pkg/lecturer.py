from cls_pkg.person import PERSON


class LECTURER(PERSON):
    def __init__(self, id, name):
        super(LECTURER, self).__init__(name)
        self.id = id
        self.name = name

    def print_id(self):
        print("Staff id: {}".format(self.id))

    def mark_ca(self):
        print("Staff id: {} has marked CA".format(self.id))

    def lecture(self):
        print("Staff id: {} has lectured".format(self.id))
