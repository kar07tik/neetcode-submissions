class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even,odd=1,0
        parity=0
        res=0

        for x in arr:
            parity ^= x & 1
            if parity:
                res += even 
                odd += 1
            else:
                res += odd
                even += 1
        return res % MOD