class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        waterH = 0
        i = 0 
        j = len(heights) - 1
        res = 0
        while (i < j):
            waterH = min(heights[i],heights[j])
            res = max((waterH * (j - i)),res)
            
            if heights[i] < heights[j]:
                i+= 1
            else:
                j -= 1
            
        return res