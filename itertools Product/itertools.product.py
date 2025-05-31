# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# Read input from the user
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute the cartesian product
result = product(A, B)

# Print the output as space-separated tuples
print(*result)

#✅ Imports the product function from Python's itertools module to compute Cartesian products.

#🧾 Reads two lines of input using input().split() and converts them into lists of integers using map(int, ...).

#🔁 Computes the Cartesian product of the two lists A and B using product(A, B).

#🧾 Stores the result as an iterator of all possible ordered pairs (tuples) from the two lists.

#🖨️ Prints the tuples using unpacking (*result) so they appear space-separated in the output.