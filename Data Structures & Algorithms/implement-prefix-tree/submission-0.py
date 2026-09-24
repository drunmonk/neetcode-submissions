class TrieNode:
    def __init__(self):
        self.childern={}
        self.EndOfWord=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        curr=self.root

        for i in word:
            if i not in curr.childern:
                curr.childern[i]=TrieNode()
            curr=curr.childern[i]
        curr.EndOfWord=True



    def search(self, word: str) -> bool:
        curr=self.root

        for i in word:
            if i not in curr.childern:
                return False
            curr=curr.childern[i]
        return curr.EndOfWord
        

    def startsWith(self, prefix: str) -> bool:

        curr=self.root

        for i in prefix:
            if i not in curr.childern:
                return False
            curr=curr.childern[i]
        return True
        
        
        