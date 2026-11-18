'''
1.
<p>Create 'tiffin_delivery_desk.py' that uses `import math` and `math.sqrt()` to find the straight-line distance in km between a kitchen at (0, 0) and a customer at (x, y), where the user types x and y as whole numbers from 0 to 20. Print the distance rounded to 1 decimal, and 'Free delivery' when it is 5 km or less. Test with (3, 4), which must give 5.0, and with (12, 5).</p>
2.
<p>Extend 'tiffin_delivery_desk.py' to price an order. Ask for the number of tiffins (1 to 40) and print the bags needed (4 tiffins per bag, rounded up with `math.ceil()`), the free tiffins earned (1 for every 5 full tiffins, with `math.floor()`) and the delivery charge (₹10 per started km, using `math.ceil()` on the distance, ₹0 if free delivery).</p>
3.
<p>Add `random.randint()` and `random.random()` to 'tiffin_delivery_desk.py'. Give every order an ID between 1000 and 9999, printed as 'TF-1234', and run a lucky draw: if `random.random()` is below 0.2, the order gets ₹50 off. Print the random value rounded to 2 decimals and whether the discount applied. Hint: `random.random()` returns a float from 0.0 up to, but not including, 1.0.</p>
4.
<p>Finish 'tiffin_delivery_desk.py' with a loop that takes 3 orders and prints a bill for each: order ID, distance, bags, free tiffins, delivery charge, discount and total at ₹70 for each paid tiffin. Test with a customer at (3, 4) for 10 tiffins, at (12, 5) for 23 tiffins and at (0, 0) for 1 tiffin. Paste the outputs as a comment at the end of the file; the random parts will differ on every run.</p>
'''