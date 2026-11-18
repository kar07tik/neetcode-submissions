from typing import List
class UnionFind:
    def __init__(self,size: int):
        self.parent=list(range(size))
        self.rank=[0]*size
        self.count=size
    def find(self,i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i,root_j = root_j,root_i
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            self.count -= 1
            return True
        return False
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n=len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False
        max_val=max(nums)
        spf=list(range(max_val+1))
        for i in range(2,int(max_val**0.5)+1):
            if spf[i] == i:
                for j in range(i*i, max_val+1,i):
                    if spf[j] == j:
                        spf[j] = i
        uf=UnionFind(n+max_val+1)
        for i , num in enumerate(nums):
            temp=num
            while temp > 1:
                p = spf[temp]
                uf.union(i,n+p)
                while temp % p == 0:
                    temp //= p
        root=uf.find(0)
        for i in range(1,n):
            if uf.find(i) != root:
                return False
        return True
        