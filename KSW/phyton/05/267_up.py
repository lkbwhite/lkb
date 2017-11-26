class Calculator:
	def __init__(self, numbers):
		self.numbers = numbers
	def sum(self):
		result = 0
		for num in self.numbers:
			result += num
		return result
	def avg(self):
		total = self.sum()
		return total / len(self.numbers)
#		return sum(self) / len(self.numbers)

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())