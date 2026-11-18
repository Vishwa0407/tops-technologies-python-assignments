# import re

# text = "My age is 25 and my brother's age is 30"
# result = re.findall(r"\d+",text)
# print(result)
# print(type(result))

# import re

# text = "Contact Number is 9876543210"
# # text1 = "Contact Number is 98765 222"

# result = re.search(r"\d{10}",text)
# # result1 = re.search(r"\d{10}",text1)
# # if result1:
# #     print("Mobile number found: ", result1.group())
# # else:
# #     print("Mobile number not found")

# if result:
#     print("Mobile number found: ", result.group())
# else:
#     print("Mobile number not found")

# import re

# text="My Mobile number is 9876543210"
# result = re.sub(r"\d{10}","XXXXXXXXXX",text)

# print(result)

# import re

# text = "Hello@Python#1234!"
# result = re.sub(r"[^a-zA-Z0-9]","",text)

# print(result)

# import re

# text = "apple,Banana;Orange"
# items = re.split(r"[,;]",text)

# print(items)

# import re 

# email = "test1@yopmail.com"
# pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# if re.fullmatch(pattern,email):
#     print("Valid email format")
# else:
#     print("Invalid email format")


import re

text = """
Admission Date : 15-08-2026
page 3
Python Programming - Regular expressions(RegEx)
Joining date : 20-09-2026

"""

dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b",text)
print(dates)
