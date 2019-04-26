class Subject:

	def __init__(self, name):
		self.name = name

	def to_dict(self):
		return {"type": __class__.__name__, "name": self.name}
