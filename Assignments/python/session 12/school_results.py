# 1. <p>Write 'school_results.py' with a dictionary `students` holding 5 fictional students (name as key, a tuple of 4 marks out of 100 as value) and a function `get_total(marks)` that returns the sum of the marks. Call it for each student in a for loop and print 'Name: total'. Constraint: Do not use the built-in `sum()`; add the marks with a loop inside the function.</p>
# 2. <p>Add a function `get_grade(percentage)` to 'school_results.py' that returns 'A' for 75 and above, 'B' for 60 to 74, 'C' for 40 to 59 and 'F' below 40, and a function `get_result(marks)` that returns the total, percentage out of 400 and grade together. Print one report line per student. Hint: Return several values with `return total, percentage, grade`. Constraint: Use positional arguments only.</p>
# 3. <p>Pick one student in 'school_results.py' and use `map()` with a lambda to add 5 grace marks to each subject, never going above 100, and `filter()` with a lambda to keep the original marks below 40. Print both results. Hint: `map()` and `filter()` return iterators, so wrap them in `list()` to print. Constraint: Each lambda must be a single expression.</p>

students = {
    "ALice": (85, 90, 78, 88),
    "Bob": (75, 80, 85, 70),
    "John": (92, 95, 89, 90),
    "Max": (65, 39, 30, 80),
    "Rachel": (88, 82, 91, 85)
}


def get_total(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total

def get_grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "F"


def get_result(marks):
    total = get_total(marks)
    percentage = (total / 400) * 100
    grade = get_grade(percentage)

    return total, percentage, grade


for name, marks in students.items():
    total, percentage, grade = get_result(marks)
    print(name, ":", "Total =", total,
          "| Percentage =", percentage,
          "| Grade =", grade)


# 3. <p>Pick one student in 'school_results.py' and use `map()` with a lambda to add 5 grace marks to each subject, never going above 100, and `filter()` with a lambda to keep the original marks below 40. Print both results. Hint: `map()` and `filter()` return iterators, so wrap them in `list()` to print. Constraint: Each lambda must be a single expression.</p>

# Pick One student
marks = students["Max"]

# Adding 5 grace marks to each subject 
grace_marks = list(map(lambda mark : min(mark + 5,100),marks))

# Filter original marks below 40
failed_marks = list(filter(lambda mark: mark < 40, marks))

print("Original Marks:", marks)
print("Grace Marks:", grace_marks)
print("Marks Below 40:", failed_marks)

# 4. <p>Finish 'school_results.py' by building a list of all totals, using `reduce` from `functools` with a lambda to find the highest total, and printing the topper's name by looping through `students`. Run the program and paste the output as a comment at the end of the file. Hint: Write `from functools import reduce` at the top of the file.</p>

from functools import reduce

# Create a list of all student totals
totals = []

for name, marks in students.items():
    total = get_total(marks)
    totals.append(total)

# Find the highest total using reduce()
highest_total = reduce(lambda a, b: a if a > b else b, totals)

for name, marks in students.items():
    if get_total(marks) == highest_total:
        print("Topper:", name)
        print("Highest Total:", highest_total)