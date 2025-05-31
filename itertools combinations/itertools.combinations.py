# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

# Read and parse input
S, k = input().split()
k = int(k)

# Sort the string to maintain lexicographic order
sorted_S = sorted(S)

# Generate combinations of size 1 to k
for i in range(1, k + 1):
    for combo in combinations(sorted_S, i):
        print(''.join(combo))

'''
🔍 Explanation:
1. from itertools import combinations
Imports the combinations() function from Python's itertools module.

This function is used to generate all possible combinations of a specified length from an iterable (like a list or string).

2. S, k = input().split()
Takes input in a single line, for example: HACK 2

Splits it into:

S = 'HACK' → the string of characters

k = '2' → the maximum combination length as a string

3. k = int(k)
Converts the input '2' (a string) into integer 2 so it can be used in loops and function calls.

4. sorted_S = sorted(S)
Sorts the characters in the string to ensure output is in lexicographic (alphabetical) order.

'HACK' → ['A', 'C', 'H', 'K']

5. for i in range(1, k + 1):
Loop from 1 to k (inclusive), to generate combinations of size 1, 2, ..., k.

6. for combo in combinations(sorted_S, i):
For each length i, it generates all possible combinations of that length from sorted_S.

7. print(''.join(combo))
Each combination is returned as a tuple of characters (e.g., ('A', 'C'))

''.join(combo) joins the tuple into a string (e.g., 'AC')

print() outputs it on a new line

'''