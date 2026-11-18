'''
1.
<p>Create 'expense_matrix.py' with a nested list `expenses` of 6 rows (January to June) and 4 columns (food, transport, rent share, entertainment), with every amount between ₹500 and ₹15,000. Use a list comprehension to build `month_totals`, one total per row, and print each month with its total. Hint: `[sum(row) for row in expenses]`; `sum()` adds up the numbers in a list.</p>
2.
<p>Add a nested list `by_category` to 'expense_matrix.py' with 4 inner lists, each holding one category's 6 monthly amounts, built with a nested list comprehension. Print each category's name with its total. Hint: The outer comprehension runs over the column numbers `range(4)`, and the inner one picks `row[c]` from every row.</p>
3.
<p>Build `big_expenses` in 'expense_matrix.py', a flat list of (month name, category name, amount) tuples for every amount above ₹5,000, using one list comprehension with two `for` clauses and an `if`. Print it one tuple per line. Hint: In a comprehension with two `for` clauses, the outer loop is written first.</p>
4.
<p>Finish 'expense_matrix.py' by building `savings_plan`, a nested list in which the transport and entertainment amounts are cut by 10% (rounded to a whole rupee) and the other columns stay the same, using a nested comprehension with a conditional expression. Print the old and new total for every month. Paste the output as a comment at the end of the file. Constraint: Do not use `append()` or loops outside comprehensions for this step.</p>

'''