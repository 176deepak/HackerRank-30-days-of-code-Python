'''
TASK
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Example

In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.

Input Format

There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array A.

Constraints
  -9 =< A[i][j] =< 9
  0 =< i, j =< 5
Output Format

Print the maximum hourglass sum in A.


#CODE

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    def Max(A):
        Maxi = 0
        R = 4
        C = 4
        if R < 4 or C < 4:
            return -1
        for i in range(R):
            for j in range(C):
                SUM = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                
                if Maxi < SUM:
                    Maxi = SUM
        return Maxi
res = Max(arr)
print(res)
