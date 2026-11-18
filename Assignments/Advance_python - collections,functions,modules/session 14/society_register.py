'''
1.
<p>Create 'society_register.py' with a function `add_flat(register, wing, flat, owner, due)` that stores {'owner': owner, 'due': due} at `register[wing][flat]`, creating the wing's inner dictionary only if the wing is new. Use a while loop that asks for these details, ends when the wing is entered as 'done', and builds `register` for a fictional society. Test with 6 flats in at least 2 wings. Hint: `if wing not in register: register[wing] = {}`.</p>
2.
<p>Add a function `record_payment(register, wing, flat, month, amount)` to 'society_register.py' that creates a 'payments' dictionary inside the flat's dictionary on the first payment, then stores month: amount in it. Print 'Flat not found' for an unknown wing or flat. Record 5 payments, including two months for one flat and one for a flat that does not exist. Constraint: Do not use try/except.</p>
3.
<p>Finish 'society_register.py' with a report that loops through `register.items()` and the flats inside each wing. For every wing, print the flats, the total dues, the total paid and the outstanding amount, followed by the outstanding amount for the whole society. Run it on your 6 flats and 5 payments and paste the output as a comment at the end of the file. Hint: A flat with no payments yet has no 'payments' key, so check `'payments' in details` first.</p>

'''