class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        indices =  {}
        for index, num in enumerate(nums):
            temp = target - num
            if temp in indices:
                return [indices[temp], index]
            indices[num] = index
        