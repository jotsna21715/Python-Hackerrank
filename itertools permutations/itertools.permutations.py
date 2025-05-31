# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

# Read input
S, k = input().split()
k = int(k)

# Generate and sort permutations
perm_list = permutations(sorted(S), k)

# Print each permutation
for p in perm_list:
    print(''.join(p))

    
'''
from itertools import permutations
➤ Imports the permutations function to generate ordered arrangements of elements.

S, k = input().split()
➤ Takes user input in the form "STRING k" (e.g., "HACK 2")
➤ Splits into S = "HACK" and k = "2" (as string)

k = int(k)
➤ Converts k to an integer.

sorted(S)
➤ Sorts the characters in the string for lexicographic order.
➤ "HACK" → ['A', 'C', 'H', 'K']

permutations(sorted(S), k)
➤ Generates all possible k-length permutations (ordered combinations without repetition).

for p in perm_list:
➤ Loops through each permutation tuple (e.g., ('A', 'C')).

print(''.join(p))
➤ Converts the tuple to a string (e.g., ('A', 'C') → "AC") and prints it.
'''