'''
TASK

Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Example

S = adbecf
Print abc def

Input Format

The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a string, S.

Constraints
  1 =< T =< 10
  length of 2 =< S =<10000
Output Format

For each String Sj (where 0 =<j =< T-1), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.
'''

#CODE

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0, n):
    string = input()
    j = 0
    while j in range(0, len(string)):
        print(string[j], end = "") 
        j += 2
    print(end = " ")
    k = 1
    while k in range(1, len(string)):
        print(string[k], end = "")
        k += 2
    
    i += 1
    print()


