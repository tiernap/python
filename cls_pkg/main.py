from cls_pkg.lecturer import LECTURER
from cls_pkg.student import STUDENT


student1 = STUDENT(1234, "sean")
student1.print_name()
student1.print_id()
student1.attend_college()
student1.sit_exams()

lecturer1 = LECTURER(4321, "joe")
lecturer1.print_name()
lecturer1.print_id()
lecturer1.lecture()
lecturer1.mark_ca()

students = [STUDENT(1, "tom"), STUDENT(2, "paul"), STUDENT(3, "Julie"), STUDENT(4, "garry"), STUDENT(5, "Emma"), STUDENT(6, "tanya"), STUDENT(7, "Robert"), STUDENT(8, "Fiachra"), STUDENT(9, "Grace"), STUDENT(10, "tintin"), STUDENT(11, "hitler"), STUDENT(12, "Donald")]

students[0].print_name()