'''
TASK
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following 3 lines:

Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.
First Element: firstElement
where firstElement is the first element in the sorted array.
Last Element: lastElement
where lastElement is the last element in the sorted array.

Input Format

The first line contains an integer, n, the number of elements in array a.
The second line contains n space-separated integers that describe a[0],a[1],......,a[n-1].

Constraints
  2 =< n =< 600
  1 =< a[i] =< 2x10^6,where 0 =< i < n.
, where .
Output Format

Print the following three lines of output:

Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.
First Element: firstElement
where firstElement is the first element in the sorted array.
Last Element: lastElement
where lastElement is the last element in the sorted array.
'''

#CODE

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    num = 0
    for i in range(n):
        numswap = 0
        for j in range(n-1):
            if(a[j]>a[j+1]):
                temp = 0
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numswap+= 1
        num = numswap+num
        if (numswap == 0):
            print("Array is sorted in",num,"swaps.\nFirst Element:",a[0],"\nLast Element:",a[-1]) 
            break
