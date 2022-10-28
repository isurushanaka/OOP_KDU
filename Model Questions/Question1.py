class Course:

	def __init__(self, cname, nlessons, cdue, npart, cfee):
		self.cname = cname
		self.nlessons = nlessons
		self.cdue = cdue
		self.__npart = npart
		self.__cfee = cfee

	def trevenue(self):
		return self.__npart*self.__cfee

	@property
	def npart(self):
		return self.__npart

	@npart.setter
	def set_npart(self,new_npart):
		self.__npart = new_npart

	@property
	def cfee(self):
		return self.__cfee

	@cfee.setter
	def set_cfee(self,new_cfee):
		self.__cfee = new_cfee

class CrashCourse(Course):
	def __init__(self, cname, nlessons, cdue, npart, cfee, duedate, location):
		super().__init__(cname, nlessons, cdue, npart, cfee)
		self.duedate = duedate
		self.location = location
		