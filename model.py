class Student(object):
	def __init__(self, first_namme, last_name, github):
		sef.first_name = first_name
		self.last_name = last_name
		self.github = github 

def get_student_by_github(github):
	sql = "select first_name, last_name, github, from students where github=?"
	row = db_execute(sql, (github,))
	s = student(row[0], row[1], row[2])
	return s

def db_execute(sql_params):
	return("Christian", "Fernandez", "chiszf")