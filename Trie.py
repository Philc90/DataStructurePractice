# implementation was based on: https://www.geeksforgeeks.org/trie-insert-and-search/
# this may be a better reference: https://albertauyeung.github.io/2020/06/15/python-trie.html

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.visitedCount = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        current = self.root
        for ch in s:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
            current.visitedCount += 1
        current.endOfWord = True

    # returns True/False depending on whether the word exists
    def search(self, s):
        current = self._search(s)
        return False if not current else current.endOfWord

    # search helper function; returns pointer to node
    def _search(self, s):
        current = self.root
        for ch in s:
            if ch not in current.children:
                return None
            current = current.children[ch]
        return current

    def countPrefixMatches(self, s):
        current = self._search(s)
        if not current:
            return 0
        return current.visitedCount

    # DFS implementation; not utilizing the visitedCount
    # just gets a pointer to the end of the prefix then do DFS
    def countPrefixMatchesDfs(self, s):
        current = self._search(s)
        if not current:
            return 0
        count = 0
        stack = [current]
        while stack:
            top = stack.pop()
            if top.endOfWord: count += 1
            for key in top.children:
                stack.append(top.children[key])
        return count

# Implementation where children are mapped to index in alphabet instead of using a dict
"""
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        current = self.root
        for ch in s:
            idx = self._chIdx(ch)

            if not current.children[idx]:
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.endOfWord = True


    def search(self, s):
        current = self.root
        for ch in s:
            idx = self._chIdx(ch)
            if not current.children[idx]:
                return False
            current = current.children[idx]
        return current.endOfWord

    def _chIdx(self, ch):
        return ord(ch) - ord('a')
"""


trie = Trie()
trie.insert('cat')
trie.insert('cats')
print(trie.search('cat'))
print(trie.search('ca'))
print(trie.countPrefixMatches('ca'))
print(trie.countPrefixMatchesDfs('ca'))