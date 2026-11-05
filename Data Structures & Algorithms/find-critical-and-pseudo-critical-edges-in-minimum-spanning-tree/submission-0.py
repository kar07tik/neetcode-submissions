class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        order=sorted((w,a,b,i) for i,(a,b,w) in enumerate(edges))

        def mst(skip: int = -1, force: int = -1) -> float:
            parent=list(range(n))

            def find(x: int) -> int:
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            total = used = 0
            if force != -1:
                a,b,w = edges[force]
                parent[find(a)] = find(b)
                total += w
                used += 1

            for w,a,b,i in order:
                if i == skip:
                    continue
                ra,rb = find(a),find(b)
                if ra != rb:
                    parent[ra] = rb
                    total += w
                    used += 1

            return total if used == n-1 else float('inf')

        base=mst()
        critical,pseudo=[],[]
        for i in range(len(edges)):
            if mst(skip=i) > base:
                critical.append(i)
            elif mst(force=i) == base:
                pseudo.append(i)
        return [critical,pseudo]












