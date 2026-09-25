class DictNode:
    def __init__(self):
        self.childern={}
        self.EndWorde=False

class WordDictionary:

    def __init__(self):
        self.root=DictNode()
        

    def addWord(self, word: str) -> None:
        curr=self.root

        for i in word:
            if i not in curr.childern:
                curr.childern[i]=DictNode()
            curr=curr.childern[i]
        curr.EndWorde=True

    def search(self, word: str) -> bool:
        def dfs(j,root):
          curr= root

          for i in range(j,len(word)):
            if word[i]=='.':
                for k in curr.childern.values():
                    if dfs(i+1,k):
                        return True
                return False
            else:
                if word[i] not in curr.childern:
                    return False
                curr=curr.childern[word[i]]
          return curr.EndWorde
        return dfs(0,self.root)
        
