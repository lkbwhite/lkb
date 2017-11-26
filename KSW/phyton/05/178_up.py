class Service:
	secret = "09 has two"
	def sum(self, a, b):
		result = a + b
		print("%s + %s = %s." %(a, b, result))


pey = Service()
pey.sum(1,1)

print(pey.secret)