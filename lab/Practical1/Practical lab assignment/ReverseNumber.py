n=int(input())
r=0
while n!=0:
	ld=n%10
	r=r*10+ld
	n=n//10

print(r)
