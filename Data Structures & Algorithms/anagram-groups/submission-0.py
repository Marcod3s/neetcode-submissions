 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for word in strs:
            sortedW = ''.join(sorted(word))
            groups[sortedW].append(word)
        return list(groups.values())