class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusts={}
        truste={}

        for k in trust:
            i=k[0]
            j=k[1]
            trusts[i] = trusts.get(i, 0) + 1
            truste[j] = truste.get(j, 0) + 1


        for i in range(n+1):
            if trusts.get(i, 0)==0:
                if truste.get(i, 0)==n-1:
                    return i
        
        return -1


