class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = []
        
        # Build trie with reversed words
        for word in words:
            node = self.trie
            for c in reversed(word):
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = True  # End marker

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        
        # Check if any suffix matches
        node = self.trie
        for i in range(len(self.stream) - 1, -1, -1):
            c = self.stream[i]
            if c not in node:
                return False
            node = node[c]
            if '#' in node:
                return True
        
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)