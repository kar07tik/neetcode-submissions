from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_text=Counter(text)
        balloon={"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        return min(count_text[char] // req for char, req in balloon.items())