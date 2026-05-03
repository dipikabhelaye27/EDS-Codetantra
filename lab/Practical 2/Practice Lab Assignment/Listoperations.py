l=[]

def Add(n1):
	l.append(n1)
	print(f"List after adding: {l}")

def Remove(n2):
	if n2 in l:
		l.remove(n2)
		print(f"List after removing: {l}")
		
	else:
		print("Element not found")

for i in range(100):
    print("""1. Add
2. Remove
3. Display
4. Quit""")

    choice=int(input("Enter choice: "))


    if choice == 1:
        n1=int(input("Integer: "))
        Add(n1)
        
    elif choice == 2:
        if len(l)==0:
            print("List is empty")
        else:
            n2=int(input("Integer: "))
            Remove(n2)
    
    elif choice == 3:
        if len(l)==0:
            print("List is empty")
        else:
            print(l)
    
    elif choice == 4:
         break
    
    else:
         print("Invalid choice")
