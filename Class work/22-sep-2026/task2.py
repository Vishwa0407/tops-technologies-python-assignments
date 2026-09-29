# swapping 

a =(int(input("Enter a number 1: ")))
b =(int(input("Enter a number 2: ")))

# a=100 
# b = 50 

# using third variable 

temp = a    #temp = 100  a=100
a=b         #a=50 b=50
b=temp      #b=100 a=50


# without using third variable

a=a+b  # 100+50  a= 150
b=a-b  # 150-50 b = 100
a=a-b   #150-100 = 50

# only using in python 
a,b=b,a

print("After swapping A:",a) 
print("After swapping B:",b) 