'''
1.
<p>Create a package folder named `hardware_shop` with an empty `__init__.py` and a module `stock.py`. In `stock.py` write `add_item(inventory, name, qty, price)`, which stores name: {'qty': qty, 'price': price} in a dictionary, and `low_stock(inventory, limit=5)`, which returns the names of items with quantity at or below the limit. In 'run_shop.py', saved next to the folder, import `stock` from the package, add 6 fictional items and print the low-stock names. Hint: Run 'run_shop.py' from the folder that contains `hardware_shop`.</p>
2.
<p>Add a module `pricing.py` to the `hardware_shop` package with `gst_amount(price, rate=18)` and `cart_total(inventory, cart)`, where `cart` is a dictionary of item name to quantity bought. `cart_total` returns the total including GST, rounded to 2 decimals, and prints a message and skips any cart item missing from the inventory. Import `pricing` in 'run_shop.py' and print the total for a cart of 3 items. Constraint: Use an `if ... in` check; do not use try/except.</p>
3.
<p>Edit `hardware_shop/__init__.py` so it imports `add_item`, `low_stock`, `gst_amount` and `cart_total` and sets `shop_name` to a shop name you invent. Rewrite 'run_shop.py' to use only `from hardware_shop import ...`, print `shop_name`, and run two carts, one valid and one containing an item that is not in stock. Paste both outputs as a comment at the end of 'run_shop.py'. Hint: Inside `__init__.py`, write `from .stock import add_item`; the dot means this package.</p>

'''