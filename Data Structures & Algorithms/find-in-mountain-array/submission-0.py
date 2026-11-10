class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        cache={}
        def get(i):
            if i not  in cache:
                cache[i]=mountainArr.get(i)
            return cache[i]
        low,high=0,n-1
        while low < high:
            mid=(low+high) // 2
            if get(mid) < get(mid+1):
                low=mid+1
            else:
                high=mid
        peak=low
        low,high=0,peak
        while low <= high:
            mid=(low+high) // 2
            val = get(mid)
            if val == target:
                return mid
            elif val < target:
                low=mid+1
            else:
                high = mid-1
        low,high=peak+1,n-1
        while low <= high:
            mid=(low+high) // 2
            val = get(mid)
            if val == target:
                return mid
            elif val > target:
                low=mid+1
            else:
                high=mid-1
        return -1