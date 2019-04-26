from subject import Subject


class Student:

	ABSENT = -1

	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		self.scores = {}

	def add_score(self, subject, date, score):
		if isinstance(score, int) and score >= Student.ABSENT:
			if subject not in self.scores.keys():
				self.scores[subject] = {}
			self.scores[subject][date] = score
		else:
			raise ValueError(int)

	def __get_score_value(self, score):
		if score == Student.ABSENT:
			return 0
		else:
			return score

	def average_in_class(self, subject, ignore_absent=False):
		if ignore_absent:
			score_sum = sum(filter(lambda x: not x == Student.ABSENT, self.scores[subject].values()))
			score_len = len(list(filter(lambda x: not x == Student.ABSENT, self.scores[subject].values())))
		else:
			score_len = len(self.scores[subject].values())
			score_sum = sum(map(lambda x: self.__get_score_value(x), self.scores[subject].values()))
		return score_sum / score_len

	def get_subject_list(self):
		return self.scores.keys()

	def average_all_subjects(self, ignore_absent=False):
		subjects = self.get_subject_list()
		sum = 0
		count = len(subjects)
		for s in subjects:
			sum += self.average_in_class(s, ignore_absent)
		average = sum/count
		return average

	def to_dict(self):
		scores = {}
		keys = self.scores.keys()
		for k in keys:
			scores[k.name] = self.scores[k]
		return {"type": __class__.__name__, "firstname": self.firstname, "lastname": self.lastname, "scores": scores}

	def get_written_name(self):
		return self.lastname + ", " + self.firstname
