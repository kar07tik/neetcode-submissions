class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        
        # Compare each word with every other word
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                # If words[i] is a substring of words[j], add it and break
                if words[i] in words[j]:
                    res.append(words[i])
                    break
                    
        return res