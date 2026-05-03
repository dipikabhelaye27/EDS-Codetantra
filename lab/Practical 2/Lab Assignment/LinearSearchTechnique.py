arr = list(map(int, input().split()))
key=int(input())
found=-1
for i in range(len(arr)):
	if arr[i]==key:
		found=i
		break

if found >=0:
	print(found)
else:
	print("Not found")

