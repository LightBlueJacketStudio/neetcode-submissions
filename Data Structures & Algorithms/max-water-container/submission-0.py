class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #edge cases
        if heights is None: return 0
        if len(heights) == 1: return 0

        #using the two pointers method
        front = 0
        back = len(heights) -1
        largest = 0
        while front < back:
            height = min(heights[front], heights[back])
            width = back - front
            curr_area = height * width
            largest = max(curr_area, largest)

            #prepare for next iteration
            if heights[front] <= heights[back]:
                front += 1
            else:
                back -= 1

        #return the largest area
        return largest
        