class TrieNode:
    #each trie node contains a dict for its children
    #and by default says its not the end of the work
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        #root is a trienode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #point at prefixTree root
        cur = self.root
        #go through character
        for c in word:
            #if character of word not in children
            #save it to a new trienode
            if c not in cur.children:
                #add it
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        #start at prefixtree root. 
        #If each char isnt in the children list 
        cur = self.root

        for c in word:
            #if we can continue to the next char do so
            #but if not return false word isnt there
            if c not in cur.children:
                return False
            cur = cur.children[c]
        #when on the last char return whether its marked as end of word or not
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        