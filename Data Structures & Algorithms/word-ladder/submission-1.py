from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words=set(wordList)
        if endWord not in words:
            return 0
        queue=deque([(beginWord,1)])
        visited = {beginWord}
        letters="abcdefghijklmnopqrstuvwxyz"
        while queue:
            word,steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in letters:
                    if ch == word[i]:
                        continue
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in words and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word,steps+1))
        return 0