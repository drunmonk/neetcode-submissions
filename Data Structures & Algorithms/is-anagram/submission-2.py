class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       d_1={}
       if len(s)!=len(t):
        return False

       for i in range(len(s)):
         d_1[s[i]]=d_1.get(s[i],0)+1
       for i in range(len(t)):
          if d_1.get(t[i],0) !=0:
            if d_1[t[i]] >0:
               d_1[t[i]]=d_1.get(t[i])-1
       for i in d_1:
          
          if d_1[i] != 0:
             return False
       return True 


        


        