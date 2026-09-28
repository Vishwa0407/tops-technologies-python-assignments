# Nested conditions if else

n1 = int(input("Enter a Number 1 : "))
n2 = int(input("Enter a Number 2 : "))
n3 = int(input("Enter a Number 3 : "))

if n1>n2:
    if n1>n3:
        print(f"{n1} is greatest !")
    else:
        print(f"{n3} is Greatest !")

else:
    if n2>n3:
        print(f"{n2} is Greatest !!")
    else:
        print(f"{n3} is Greatest !!")