from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold the grouped anagrams
        # Key: tuple representing character counts, Value: list of strings
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Initialize a count array of size 26 for 'a' through 'z'
            count = [0] * 26
            
            # Count the frequency of each character in the string
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Tuples are immutable and hashable, so they can be used as dictionary keys
            anagram_map[tuple(count)].append(s)
            
        # Return all the grouped anagrams as a list of lists
        return list(anagram_map.values())