class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 1
        map = set(nums)
        
        if len(nums) == 0: return 0

        for num in nums:
            
            if (num - 1) not in map:
                temp = 0
                while num + temp in map:
                    temp+=1
                res = max(res, temp)
        
        return res

                
