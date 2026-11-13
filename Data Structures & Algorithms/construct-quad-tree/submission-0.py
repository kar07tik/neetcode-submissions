"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(r,c,size):
            if size == 1:
                return Node(grid[r][c] == 1, True, None,None,None,None)
            half=size // 2
            tl=build(r,c,half)
            tr=build(r,c+half,half)
            bl=build(r+half,c,half)
            br=build(r+half,c+half,half)

            if(tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf
                    and tl.val == tr.val == bl.val == br.val):
                return Node(tl.val, True,None,None,None,None)
            return Node(True,False,tl,tr,bl,br)
        return build(0,0,len(grid))














        