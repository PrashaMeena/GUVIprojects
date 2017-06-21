import sys
for line in sys.stdin:
	num = int(line) 
if num%2 == 0:
  print("even")
else:
  print("odd")
