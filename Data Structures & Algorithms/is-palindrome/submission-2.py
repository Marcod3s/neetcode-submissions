import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        temp = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        j = len(temp) -1 
        for i in range(len(temp)):
            if temp[i] != temp[j]:
                return False
            j -= 1
        return True