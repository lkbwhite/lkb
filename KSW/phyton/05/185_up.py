class Service:
	secret = "09 has two"
	def __init__(self, name):
		self.name = name
	def sum(self, a, b):
		result = a+b
		print("%s is %s + %s = %s." % (self.name, a, b, result))



pey = Service("lyan")
pey.sum(1,1)