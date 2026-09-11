from collections import Counter
from typing import List


class Solution:

  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    # Group numbers by their frequency
    for num, freq in count.items():
      buckets[freq].append(num)

    res = []
    # Traverse buckets in reverse (highest frequency first)
    for freq in range(len(buckets) - 1, 0, -1):
      for num in buckets[freq]:
        res.append(num)
        if len(res) == k:
          return res