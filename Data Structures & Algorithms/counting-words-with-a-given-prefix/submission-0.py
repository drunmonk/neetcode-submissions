class Node:

    def __init__(self):
      self.childern={}
      self.count=0

class Trie:
    def __init__(self):
        self.root=Node()
    def add(self,word):
        curr=self.root
        for i in word:
         if i not in curr.childern:
            curr.childern[i]=Node()
         curr=curr.childern[i]
         curr.count+=1
    def count(self,pref):
        curr=self.root
        for i in pref:
            if i not in curr.childern:
              return  0
            curr=curr.childern[i]
        return curr.count


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        t=Trie()

        for i in words:
            if len(i)>=len(pref):
               t.add(i)
        
        return t.count(pref)

        