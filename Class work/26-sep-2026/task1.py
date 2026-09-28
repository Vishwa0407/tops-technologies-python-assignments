# and : Must be true all 
# or : Anyone condition


n1=int(input("Enter a number 1 : "))
n2=int(input("Enter a number 2 : "))
n3=int(input("Enter a number 3 : "))

if n1>n2 and n1>n3:
    print("Number 1 is Greatest")

elif n2>n1 and n2>n3:
    print("Number 2 is greatest")

else:
    print("Number 3 is greatest")