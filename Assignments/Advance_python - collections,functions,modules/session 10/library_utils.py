'''
1.
<p>Create a module file named 'library_utils.py' with a function `days_late(issue_day, return_day)`, which returns how many days a book is late when it is kept more than 14 days (0 if not late), and `fine_amount(late_days, per_day=2)`, which returns the fine in ₹. In 'library_main.py', saved in the same folder, use `import library_utils` and print the fine for a book issued on day 10 and returned on day 31. Hint: Run 'library_main.py', not the module. Constraint: Do not call `print()` or `input()` at the top level of the module.</p>
2.
<p>Add `issue_book(register, member, title, issue_day)` and `books_of(register, member)` to 'library_utils.py'. `issue_book` appends a dictionary with those four details to the `register` list, and `books_of` returns the titles issued to that member. In 'library_main.py', bring them in with `from library_utils import issue_book, books_of`, issue 5 books to 3 invented members and print each member's titles.</p>
3.
<p>Finish the program by adding the constant `LOAN_DAYS = 14` to 'library_utils.py' and using it inside `days_late`. In 'library_main.py', switch to `import library_utils as lib` and add a while-loop menu (1 Issue book, 2 Return book and show fine, 3 Exit). Test a return on time, a return 7 days late and a return 30 days late. Paste the outputs as a comment at the end of 'library_main.py'. Hint: `as lib` gives the module a short name, used like `lib.LOAN_DAYS`.</p>

'''