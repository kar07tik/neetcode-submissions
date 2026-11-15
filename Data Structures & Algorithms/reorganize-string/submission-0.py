class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt=Counter(s)
        if max(cnt.values()) > (len(s)+1) // 2:
            return ""
        heap=[(-c,ch) for ch , c in cnt.items()]
        heapq.heapify(heap)
        res=[]
        prev=None
        while heap:
            c,ch=heapq.heappop(heap)
            res.append(ch)
            if prev:
                heapq.heappush(heap,prev)
                prev=None
            c += 1
            if c < 0:
                prev = (c,ch)
        return "".join(res)