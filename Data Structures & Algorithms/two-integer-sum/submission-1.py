class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # edge cases / impossible cases
        # either input is None, return empty list
        if not nums: return [] # target could be 0
        dict = {} # empty dictionary for storing pairs
        # residual = 0 # variable to store the conter part of a number
        # normal cases
        for index, num in enumerate(nums):
            if num in dict: # means we found a pair
                index1 = dict.get(num) # retrive the index
                return [index1, index] # we can use index1 at front directly
                # since the smaller index is always in the dict first
            else:
                dict[target - num ] = index # store the current index as the value
                # under the key of the residual


        return [] # if no pair is found, not possible in the problem tho
