'''
1.
<p>Create 'canteen_lambdas.py' with a list `menu` of 8 tuples for a fictional college canteen: (item name, price in ₹, is_veg True or False). Write one lambda that takes a menu tuple and returns a tuple of the item name in capitals and its price with 5% GST rounded to 2 decimals. Use `map()` with it and print the results. Hint: `map()` returns an iterator; wrap it in `list()` before printing.</p>
2.
<p>Add a lambda to 'canteen_lambdas.py' that is `True` only for vegetarian items priced at ₹60 or less. Use it with `filter()` on `menu` and print the items that remain. Make sure at least 3 items pass and at least 3 fail the test. Hint: `filter()` also returns an iterator, so convert it with `list()`.</p>
3.
<p>Finish 'canteen_lambdas.py' with a function `order_total(prices)` that uses `reduce()` with a lambda to add up the prices of an order, and a second lambda with a conditional expression that takes ₹15 off only when the total is above ₹200. Test with orders totalling ₹180, ₹200 and ₹260, and paste the outputs as a comment at the end of the file. Hint: Import it with `from functools import reduce`. Constraint: Each lambda must hold one expression only.</p>

'''