### My solution...
One way to think about the problem is to compare every maximum profit for every instance of a new minimum price.
We can think of this as having a partition of the main list where a new sublist is created whenever a lower price is found, and higher prices are added to the sublist.

i.e., ***main_list*** = [3, 4, 2, 4, 5, 4, 1, 2] -> stock prices/input list.

This gives us ***partition*** = [ [3, 4], [2, 4, 5, 4], [1, 2] ] -> a sublist for every minimum, where we can calculate profits by pairing the first element of each sublist (minimum) with every other element in their respective sublist.
> In the example above, ***partition***[1] has possible profits 4-2, 5-2, and 4-2, where 2 is the first element and minimum in that sublist. 

The point is, the minimum in ***partition***[0] is no longer needed to calculate profits in ***partition***[1]
> Comparing minimums, 2 < 3 => 4-2 > 4-3, where 4 is one of the prices in ***partition***[1], implying that profits using 2 as the minimum will always be greater than profits using 3 as the minimum.

### In short, 
we are finding both the minimum price in the list and the maximum profit between two prices in one iteration, but the final minimum price does not necessarily contribute to the final maximum profit.

This allows us to work forwards (left to right in a list, no back and forths) and iterate over the ***main_list*** in O(n) time.

> The partition representation is made to explicitly break down the general idea of my program. The program itself implicitly works on these ideas and does not physically create these partitions.

### How to run...
solution.py can be run as a standalone with python solution.py, or as a module by importing findProfit(). The function takes in a list (array) of numbers representing stock prices in the (i+1)th day. Returns an int which is the maximum profit.
When running solution.py as a standalone, we have 3 options:

**U** - user inputs; we can enter the list through the terminal, separated by spaces, and it runs findProfit() with the entered list.
**T** - runs findProfit() to test with hardcoded inputs which include the example lists in the instructions.
**E/X** - exits the program.

These selections can be entered without capslock.