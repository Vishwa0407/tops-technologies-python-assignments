# Odd and even using while loop 

i = 1
ev=0
od=0
evsum=0
odsum=0
sum=0

while(i <= 5):
    n = int(input("Enter a Number: "))
 
    if(n%2 == 0):
        print("Even !!")
        ev=ev + 1
        evsum= evsum + n
    else:
        print("Odd!!")
        od = od + 1
        odsum = odsum + n

    sum = sum + n
    i = i + 1

print("Even numbers count :",ev)
print("od numbers count :",od)
print("Even numbers Sum :",evsum)
print("odd numbers Sum :",odsum)
print("Total sum",sum)