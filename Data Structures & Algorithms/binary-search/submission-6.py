class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        high = len(nums) -1
        low = 0

        mid = int(((high-low)/2 + low))

        while low <= high:
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1 
            elif nums[mid] == target:
                return mid
            mid = int(((high-low)/2 + low))
        
        return -1
