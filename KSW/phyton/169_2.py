#169_2

f = open("/Users/SW/Desktop/study/KSW/phyton/sample.txt", 'r')
totalSum = 0
totalAvg = 0
count = 0
while True:
	line = f.readline()
	if not line : break
	totalSum += int(line)
	count += 1

totalAvg = float(totalSum / count)
f.close()

f = open("/Users/SW/Desktop/study/KSW/phyton/result.txt", 'w')
tmpStr = "sum : %d avg : %0.2f" %(totalSum, totalAvg)
f.write(tmpStr)
f.close()