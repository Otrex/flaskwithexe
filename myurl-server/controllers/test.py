
from models.test import students

class Test:
	@staticmethod
	def get_students():
		studs = [ student.name for student in students.query.all() ]
		return ', '.join(studs)