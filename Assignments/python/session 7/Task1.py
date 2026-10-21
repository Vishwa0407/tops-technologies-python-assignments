# 1.Write a Python program that loops through a list of fruits: ['Apple', 'Banana', 'Mango', 'Orange'] and prints each fruit, but uses the continue statement to skip printing 'Banana'.

fruits = ['Apple', 'Banana', 'Mango', 'Orange']

for fruit in fruits:
    if fruit == "Banana":
        continue
    
    print(fruit)