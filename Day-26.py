'''
Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0).
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date,
fine = 15 Hackos X (the number of days late).
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the
fine = 500 Hackos X (the number of months late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.

Input Format
  The first line contains 3 space-separated integers denoting the respective day, month, and year on which the book was actually returned.
  The second line contains 3 space-separated integers denoting the respective day, month, and year on which the book was expected to be returned (due date).

Constraints
  1 <=D<= 31
  1 <=M<= 12
  1 <=Y<= 3000
  It is guaranteed that the date will be valid Gregorian calendar date.
  
Output Format
  Print a single integer denoting the library fine for the book received as input.

'''

#CODE

actual = input()
actual = list(map(int, actual.split(" ")))
expected = input()
expected = list(map(int, expected.split(" ")))
actualDate = actual[0]
actualMonth = actual[1]
actualYear = actual[2]
expectedDate = expected[0]
expectedMonth = expected[1]
expectedYear = expected[2]
fine = 0
if actualYear > expectedYear:
    fine = 10000
elif actualYear == expectedYear: #Same calender year
    if actualMonth > expectedMonth: #checking months
        fine = 500 * (actualMonth - expectedMonth)
    elif actualMonth == expectedMonth: #check dates now
        if actualDate > expectedDate:
            fine = 15 * (actualDate - expectedDate)
print(fine)

