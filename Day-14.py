'''
Task
Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and saves it to the __elements instance variable.
A computeDifference method that finds the maximum absolute difference between any 2 numbers in __elements and stores it in the maximumDifferenece instance variable.
Input Format

You are not responsible for reading any input from stdin. The locked Solution class in the editor reads in 2 lines of input. The first line contains N, the size of the elements array. 
The second line has N space-separated integers that describe the __elements array.

Constraints
  1 =< N =< 10
  1 =< __elements[i] =< 100, 0 =< i =< N-1
, where 
Output Format

You are not responsible for printing any output; the Solution class will print the value of the maximumDifference instance variable.
'''

#CODE
class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        maxi = 0
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                absolute = abs(self.__elements[i] - self.__elements[j])
                if absolute > maxi:
                    maxi = absolute
        self.maximumDifference = maxi
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
