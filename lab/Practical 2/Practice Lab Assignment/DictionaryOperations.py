# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

print("Original Dictionary:",student)

key1=int(input())
value1=input()
student[key1]=value1
print("After Insertion:",student)

key2=int(input())
value2=input()
student.update({key2:value2})
print("After Update:",student)

key3=int(input())
student.pop(key3,None)
print("After Deletion:",student)

print("Traversing Dictionary:")
for k,v in student.items():
	print(k,":",v)
