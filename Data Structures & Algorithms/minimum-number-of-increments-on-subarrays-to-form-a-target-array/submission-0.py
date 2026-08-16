class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # We need at least target[0] operations for the first element
        operations = target[0]
        
        # Iterate through the rest of the array
        for i in range(1, len(target)):
            # If the current element is greater than the previous one,
            # we need additional operations to reach the current target value.
            # If it's smaller or equal, we can just "reuse" the increments 
            # from the previous element by extending the subarray.
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
                
        return operations