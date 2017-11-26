class HousePark:
	lastname = 'park '
	def __init__(self, name):
		self.fullname = self.lastname + name
	def travel(self, where):
		print("%s, go to %s." %(self.fullname, where))

pey = HousePark('application')
#pey.setname('application')

print(pey.fullname)

pey.travel('seoul')

class HouseKim(HousePark):
	lastname = "kim"
	def travel(self, where, day):
		print("%s, %s where %sday." % (self.fullname, where, day))
juliet = HouseKim("juliet")
juliet.travel("dokdo", 3)

juliet = HouseKim("juliet")
juliet.travel("dokdo", 3)