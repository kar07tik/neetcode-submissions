class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            # Check if there is a conflicting mapping
            if ((c1 in mapST and mapST[c1] != c2) or 
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            
            # Create the mapping
            mapST[c1] = c2
            mapTS[c2] = c1
            
        return True