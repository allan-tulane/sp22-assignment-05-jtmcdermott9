# CMPS 2200 Assignment 5
## Answers

**Name:**__JT McDermott_____________________


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**
The greedy algorithm is to select the largest Geometrica denomination possible, then subtract the amount from the total USD and repeat until all of the currency has been exchanged. This algorithm is optimal as the largest possible denomination is always a part of the optimal solution set.

1b.
This implementation has O(n) work and span.






- **2a.**
  Consider trying to make change for 10 USD in a currency denominated with 2, 4, 7. The minimum number of coins to make perfect change is 3 (2+4+4), which does not contain 7, the largest denomination because it is impossible to make perfect change if 7 is included in this example.

2b. 

To find the minimum number of coins of an arbitrary denomination conversion, we can use an approach where we check the the values of each of the denominations from smallest to greatest, find the minimum number of coins and subtract the value from the total value and continue checking, insuring to check that at each step it is possible by comparing to infinity and the previous result.
The work is O(cn) where c is the number of different denominations, and the span is simply O(n)


