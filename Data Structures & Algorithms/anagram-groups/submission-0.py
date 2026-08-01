class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups={} # store strings by anagram groups (group is defined by strings common sorted value)
        for string in strs:
            sorted_string=''.join(sorted(string))
            if sorted_string not in anagram_groups:
                anagram_groups[sorted_string]=[]

            anagram_groups[sorted_string].append(string)
        
        return list(anagram_groups.values())

        