from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize frequency map with the first word
        common_counts = Counter(words[0])
        
        # Intersect character frequencies across all words
        for word in words[1:]:
            common_counts &= Counter(word)
            
        # Expand character counts into a list of characters
        res = []
        for char, count in common_counts.items():
            res.extend([char] * count)
            
        return res