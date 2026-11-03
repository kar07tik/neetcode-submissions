from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        parent=list(range(n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a,b):
            ra,rb=find(a),find(b)
            if ra != rb:
                parent[rb] = ra

        owner={}
        for i,acc in enumerate(accounts):
            for email in acc[1:]:
                if email in owner:
                    union(owner[email],i)
                else:
                    owner[email]=i
        groups=defaultdict(set)
        for email,i in owner.items():
            groups[find(i)].add(email)

        return [[accounts[root][0]] + sorted(emails)
                for root,emails in groups.items()]








