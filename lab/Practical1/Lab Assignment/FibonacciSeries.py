def fibonacci(n):

# 	# write the code..

# 		return fibonacci(   ) 


# n = int(input())
# for i in range(1, n + 1):
# 	print(fibonacci(i), end=" ")
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		f=fibonacci(n-1)+fibonacci(n-2)
		return f

#return fibonacci(   ) 
def order(n):
	for i in range(n):
		print(fibonacci(i), end=" ")

n = int(input())
# for i in range(1, n + 1):
# 	print(fibonacci(i), end=" ")
order(n)
