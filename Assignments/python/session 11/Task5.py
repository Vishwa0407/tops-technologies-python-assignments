# 5. Build a function update_cart(cart, item, qty) that adds a new item to a Flipkart-style cart dictionary or updates the quantity if the item already exists, then returns the updated cart.<br><br><em><strong>Hint:</strong> Use the dictionary's update() method or direct assignment for adding/updating entries.</em>

def update_cart(cart, item, qty):
    cart[item] = qty
    return cart


my_cart = {
    "Laptop": 1,
    "Mouse": 2
}

print(update_cart(my_cart, "Keyboard", 1))