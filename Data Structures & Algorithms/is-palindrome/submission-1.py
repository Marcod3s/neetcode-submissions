import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        a = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        j = len(a) -1
        for i in range(len(a)):
            if a[i] != a[j]:
                return False
            j -= 1
        return True