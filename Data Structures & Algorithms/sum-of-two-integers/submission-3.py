""" Problem:
Given two integers a and b, 
return the sum of the two integers 
without using the + and - operators.
"""

# general idea
# cannot use + or -
# use len() then

# algorithm ?

# time complexity
# O(1) since we just call len()
# space complexity
# O(n) since we will address N elements

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # edge cases / impossible cases
        if not a and not b: return 0 # a and b are both 0

        # normal cases
        turn = 1 # used to mark if teh sign needs to change

        if a < 0 and b < 0: 
            a *= -1
            b *= -1
            turn = -1

        # pick the small number to loop
        small = min(a,b)
        big = max(a,b)

        list1 = [0] * big or []
        if small >= 0:
            for _ in range(small):
                list1.append([0])
        if small < 0:
            for _ in range(-1 * small):
                if list1 and turn != -1: list1.pop() # if we still have elements
                else: 
                    turn = -1 # indicate negative
                    list1.append([0])


        return len(list1) * turn