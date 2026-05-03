import math

n = int(input())
digits = len(str(n))

if digits ==1:
	print(n**2)
elif digits == 2:
	result = math.sqrt(n)
	print(f"{result:.2f}")
elif digits == 3:
	result = n**(1/3)
	print(f"{result:.2f}")
else:
	print("Invalid")
	
