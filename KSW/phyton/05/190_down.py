class FourCal:
	def setdata(self, first, second):
		self.first = first
		self.second = second
	def sum(self):
		result = self.first + self.second
		return result
	def mul(self):
		result = self.first * self.second
		return result
	def sub(self):
		result = self.first - self.second
		return result
	def div(self):
		result = self.first / self.second
		return result		
a = FourCal()
a.setdata(4, 2)

print(a.first)
print(a.second)

b = FourCal()
b.setdata(3, 7)
print(b.first)
print(b.second)

print(a.sum())
print(b.sum())

print(a.mul())
print(b.mul())


print(a.sub())
print(b.sub())

print(a.div())
print(b.div())
