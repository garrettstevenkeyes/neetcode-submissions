class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        #iterate through chars 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            #base case
            if idx == len(word):
                return node.endOfWord
            
            c = word[idx]
            #if it is period and can be any char
            if c == '.':
                for cn in node.children.values():
                    if dfs(cn, idx+1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], idx + 1)
        return dfs(self.root, 0)



# def dfs(node, idx):
#             #base case, end of word
#             if idx == len(word):
#                 return node.endOfWord
            

#             if c == '.':
#                 #try every child for this position
#                 for nxt in node.children.values():
#                     if dfs(nxt, idx+1):
#                         return True
#                 return False
            
#             else:
#                 if c not in node.children:
#                     return False
#                 return dfs(node.children[c], idx+1)
#         return dfs(self.root, 0)

