from student import Student

students = []

studentA = Student("Max", "Mustermann")
studentA.add_score("Magic", "30.02.3019", 30)
studentA.add_score("Magic", "31.02.3019", 100)
studentA.add_score("Magic", "01.03.3019", Student.ABSENT)
studentA.add_score("Magic", "02.03.3019", 0)
studentA.add_score("Magic", "03.03.3019", 50)
studentA.add_score("PitE", "03.03.3019", 22)
studentA.add_score("PitE", "03.03.3019", 23)
studentA.add_score("PitE", "03.03.3019", 100)
studentA.add_score("PitE", "03.03.3019", Student.ABSENT)
students.append(studentA)

me = Student("Julian", "Knorr")
me.add_score("PitE", "29.03.2019", 100)
me.add_score("PitE", "29.03.2019", 100)
me.add_score("PitE", "05.04.2019", 100)
me.add_score("PitE", "12.04.2019", 100)
me.add_score("PitE", "19.04.2019", Student.ABSENT)
students.append(me)

print("Average of " + studentA.firstname + " " + studentA.lastname + " in Magic (ignoring absents): " + str(studentA.average_in_class("Magic", True)))
print("Average of " + studentA.firstname + " " + studentA.lastname + " in Magic (absent = 0): " + str(studentA.average_in_class("Magic", False)))
