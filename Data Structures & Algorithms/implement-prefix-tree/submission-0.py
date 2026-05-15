class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #get the root
        cur = self.root
        #iterate through letters of word
        for c in word:
            #if the letter does not exists in the children dict add it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            #jump to the letter
            cur = cur.children[c]
        #at the end of the word, mark the end of word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        #start at the root
        cur = self.root
        #iterate through word characters
        for c in word:
            #if its not in the children return False
            if c not in cur.children:
                return False
            #otherwise jump there
            cur = cur.children[c]
        #if the last char in the word is not marked end of word its false
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        