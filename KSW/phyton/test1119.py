#169_2
f = open("/Users/SW/Desktop/study/KSW/phyton/sample.txt", 'r')
lines = f.readlines()
f.close()

total = 0
for line in lines:
	score = int(line)
	total += score

average = total/len(lines)
f = open("/Users/SW/Desktop/study/KSW/phyton/result2.txt", 'w')
f.write("%f" %average)
f.close()