from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = defaultdict(list)
        for u,t,w in sorted(zip(username,timestamp,website), key=lambda x: x[1]):
            visits[u].append(w)
        count=defaultdict(int)
        for sites in visits.values():
            for pattern in set(combinations(sites,3)):
                count[pattern] += 1

        best = min (count, key=lambda p: (-count[p],p))
        return list(best)