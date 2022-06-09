'''
Task
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given a number, n, determine and print whether it is Prime or Not prime.

Note: If possible, try to come up with a O(n^1/2) primality algorithm, or see what sort of optimizations you come up with for an O(n) algorithm. Be sure to check out the Editorial after submitting your code.

Input Format

The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines contains an integer, n, to be tested for primality.

Constraints
  1 <=T<= 30
  1 <=n<= 2x10^9
  
Output Format
  For each test case, print whether n is Prime or Not prime on a new line.
  
'''

#CODE

from math import sqrt
from sys import stdin

def checkPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i is 0:
            return False
    return True
n = int(input())
for line in stdin:
    val = int(line)
    if (val >= 2 and checkPrime(val)):
        print("Prime")
    else:
        print("Not prime")
