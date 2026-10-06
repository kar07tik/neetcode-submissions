class TrieNode:
    def __init__(self):
        self.children = {}  # Map character to TrieNode
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            curr = node
            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    # Try all possible child nodes for wildcard '.'
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.is_end_of_word

        return dfs(0, self.root)


# Example usage:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("day")
# wordDictionary.addWord("bay")
# wordDictionary.addWord("may")
# wordDictionary.search("say") # returns False
# wordDictionary.search("day") # returns True
# wordDictionary.search(".ay") # returns True
# wordDictionary.search("b..") # returns True