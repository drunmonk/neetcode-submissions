class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd={}
        td={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            sd[s[i]]=1+sd.get(s[i],0)
            td[t[i]]=1+td.get(t[i],0)
        
        for c in sd:
            if sd[c] != td.get(c,0):
                return False
        return True
            
        


        