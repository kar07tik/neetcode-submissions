class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities={src for src, _ in paths}
        for _, dst in paths:
            if dst not in start_cities:
                return dst
        return ""
