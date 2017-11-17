"""
2017.11.17
KIM SEWOONG
P.106
"""

#Q1
"""
881120-1068234 => (YYYYMMDD) 
use charcater slice
"""

pin = "881120-1068234"
yyyymmdd = pin[0:6]
num = pin[:6]+pin[7:]
#num = pin.replace('-', '')
print(yyyymmdd)
print(num)
