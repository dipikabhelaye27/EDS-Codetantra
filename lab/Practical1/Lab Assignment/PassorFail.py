n=int(input())

data=list(map(int,input().split()))

sum=0
count=0
for i in data:
	if i<40:
		count=count+1

if count==1:
	print("Fail")
else:
	for i in data:
		sum+=i
		p=sum/n
	print("Aggregate Percentage:",f"{p:.2f}")

	if p>=75:
		print("Grade: Distinction")
	elif p>=60 and p<75:
		print("Grade: First Division")
	elif p>=50 and p<60:
		print("Grade: Second Division")
	elif p>=40 and p<50:
		print("Grade: Third Division")
