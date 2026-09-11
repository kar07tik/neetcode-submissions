class Solution:
    def encode(self, strs: list[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the delimiter '#' separating length and content
            j = s.find('#', i)
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res