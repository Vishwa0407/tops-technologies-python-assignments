'''
Create a program that uses a while loop to print a pyramid star pattern with 4 rows, so the output looks like BookMyShow's seat rows:
*
***
*****
*******<br><br><em><strong>Hint:</strong> Use two nested while loops: one for spaces, one for stars.</em>
'''

row = 1

while row <= 4:
    spaces = 4 - row
    stars = 2 * row - 1

    while spaces > 0:
        print(" ", end="")
        spaces -= 1

    while stars > 0:
        print("*", end="")
        stars -= 1

    print()
    row += 1