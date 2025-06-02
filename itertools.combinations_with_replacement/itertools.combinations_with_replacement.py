from itertools import combinations_with_replacement

# Read input string and integer
S, k = input().split()
k = int(k)

# Sort the string to ensure combinations are in lexicographic order
sorted_S = sorted(S)

# Generate combinations with replacement
combos = combinations_with_replacement(sorted_S, k)

# Print each combination as a string
for c in combos:
    print(''.join(c))

'''

Explanation in Points:
from itertools import combinations_with_replacement
➤ Imports the function that generates combinations where elements can repeat (e.g., 'AA', 'CC').

S, k = input().split()
➤ Takes input from the user in one line, like: "HACK 2"
➤ Splits into:

S = 'HACK' → the string

k = '2' → the number (as a string)

k = int(k)
➤ Converts k from a string to an integer.

sorted_S = sorted(S)
➤ Sorts the characters of the string alphabetically for lexicographic output.
➤ 'HACK' → ['A', 'C', 'H', 'K']

combos = combinations_with_replacement(sorted_S, k)
➤ Generates all possible length-k combinations where characters can repeat and order is non-decreasing.

for c in combos:
➤ Loops over each combination tuple (e.g., ('A', 'A'), ('A', 'C'))

print(''.join(c))
➤ Joins characters in the tuple into a string (e.g., ('A', 'C') → 'AC')
➤ Prints each combination on a new line
'''