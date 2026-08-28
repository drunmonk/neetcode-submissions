class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            s=[0]*26
            for j in i:
                s[ord(j)-ord('a')]+=1
            s=tuple(s)
            if s in d:
                d[s]+=[i]
            else:
                d[s]=[i]
        return list(d.values())
                
                

        