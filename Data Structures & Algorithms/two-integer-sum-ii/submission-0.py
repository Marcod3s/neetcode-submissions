class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        j = len(numbers) -1
        i = 0
        
        sum = numbers[i] + numbers[j]
        while sum != target :
            if sum > target:
                j -= 1
            else: 
                i += 1 
            sum = numbers[i] + numbers[j]
        solution = [i + 1,j + 1]
        return solution