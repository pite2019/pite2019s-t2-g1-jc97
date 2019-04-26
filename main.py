from student import Student
from subject import Subject
from json import *
import os


def json_prepare(subjects, students):
	data = {"subjects": [], "students": []}
	for s in subjects:
		data["subjects"].append(s.to_dict())
	for s in students:
		data["students"].append(s.to_dict())
	return data


def decode(data):
	subjects = []
	students = []
	for s in data["subjects"]:
		subjects.append(Subject(s["name"]))
	for s in data["students"]:
		student_append = Student(s["firstname"], s["lastname"])
		scores = s["scores"]
		score_keys = scores.keys()
		for subject_name in score_keys:
			subject_obj = None
			for o in subjects:
				if o.name == subject_name:
					subject_obj = o
			student_append.scores[subject_obj] = scores[subject_name]
			students.append(student_append)
	return (subjects, students)


def main():
	db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "default.txt")
	f = open(db_path, 'r')

	json_data = f.read()
	f.close()
	data = loads(json_data)
	subjects, students = decode(data)

	# magic = Subject("Magic")
	# pite = Subject("PitE")
	# subjects = [magic, pite]
	#
	# students = []
	#
	# studentA = Student("Max", "Mustermann")
	# studentA.add_score(magic, "30.02.3019", 30)
	# studentA.add_score(magic, "31.02.3019", 100)
	# studentA.add_score(magic, "01.03.3019", Student.ABSENT)
	# studentA.add_score(magic, "02.03.3019", 0)
	# studentA.add_score(magic, "03.03.3019", 50)
	# studentA.add_score(pite, "03.03.3019", 22)
	# studentA.add_score(pite, "03.03.3019", 23)
	# studentA.add_score(pite, "03.03.3019", 100)
	# studentA.add_score(pite, "03.03.3019", Student.ABSENT)
	# students.append(studentA)
	#
	# me = Student("Julian", "Knorr")
	# me.add_score(pite, "29.03.2019", 100)
	# me.add_score(pite, "29.03.2019", 100)
	# me.add_score(pite, "05.04.2019", 100)
	# me.add_score(pite, "12.04.2019", 100)
	# me.add_score(pite, "19.04.2019", Student.ABSENT)
	# students.append(me)

	print("Average of student %s in %s (ignoring absents): %5.2f" % (students[0].get_written_name(), subjects[0].name,
																	 students[0].average_in_class(subjects[0], True)))
	print("Average of student %s in %s (absent = 0): %5.2f" % (students[0].get_written_name(), subjects[0].name,
															   students[0].average_in_class(subjects[0], False)))
	print("Average of student %s in all subjects (absent = 0): %5.2f" % (students[0].get_written_name(),
																		 students[0].average_all_subjects(False)))

	print("")
	print("Adding more test data...")
	subjects, students = add_test_data(subjects, students)
	print("")
	print("Exportiere zu JSON.....")

	data = json_prepare(subjects, students)
	json_data = dumps(data)

	print(json_data)

	f = open("output.py.txt", 'w')
	f.write(json_data)
	f.close()


def add_test_data(subjects, students):
	subjects.append(Subject("German"))

	students.append(Student("Donald", "Duck"))
	students[len(students) - 1].add_score(subjects[1], "01.01.2019", Student.ABSENT)
	students[len(students) - 1].add_score(subjects[2], "01.01.2019", Student.ABSENT)

	students.append(Student("Test", "Student"))
	students[len(students) - 1].add_score(subjects[0], "01.06.2030", 90)
	students[len(students) - 1].add_score(subjects[2], "0w.07.2023", 44)

	students.append(Student("Klaus", "Muster"))
	students[len(students) - 1].add_score(subjects[0], "01.04.2019", 77)
	students[len(students) - 1].add_score(subjects[2], "03.03.2019", Student.ABSENT)
	students[len(students) - 1].add_score(subjects[2], "10.03.2019", 64)
	students[len(students) - 1].add_score(subjects[2], "17.03.2019", 20)

	students.append(Student("Test", "Studentin"))
	students[len(students) - 1].add_score(subjects[0], "01.06.2030", 90)
	students[len(students) - 1].add_score(subjects[2], "0w.07.2023", 44)

	students.append(Student("Muster", "Studentin"))
	students[len(students) - 1].add_score(subjects[0], "01.06.2030", 90)
	students[len(students) - 1].add_score(subjects[2], "0w.07.2023", 44)

	students.append(Student("Muster", "Student"))
	students[len(students) - 1].add_score(subjects[0], "01.06.2030", 91)
	students[len(students) - 1].add_score(subjects[2], "0w.07.2023", 33)

	students.append(Student("Debug", "Studentin"))
	students[len(students) - 1].add_score(subjects[0], "01.06.2030", 90)
	students[len(students) - 1].add_score(subjects[0], "0w.07.2023", 44)

	students.append(Student("Debug", "Studentin"))
	students[len(students) - 1].add_score(subjects[1], "01.06.2030", 90)
	students[len(students) - 1].add_score(subjects[2], "0w.07.2023", 44)

	students.append(Student("Debug", "Student"))
	students[len(students) - 1].add_score(subjects[0], "01.06.2030", 91)
	students[len(students) - 1].add_score(subjects[1], "0w.07.2023", 33)

	students.append(Student("Thomas", "Muster"))
	students[len(students) - 1].add_score(subjects[0], "01.04.2019", 77)
	students[len(students) - 1].add_score(subjects[2], "03.03.2019", Student.ABSENT)
	students[len(students) - 1].add_score(subjects[2], "10.03.2019", 64)
	students[len(students) - 1].add_score(subjects[2], "17.03.2019", 20)

	return subjects, students


if __name__ == "__main__":
	main()
