class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        candidates.sort()

        def dfs(i,ar,total):

            if sum(ar)==target:
                res.append(ar.copy())
                return
            if i==len(candidates) or total>target:
                return 
            
            ar.append(candidates[i])
            dfs(i+1,ar,total+candidates[i])
            ar.pop()

            while i+1<len(candidates) and      candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,ar,total)
        
        dfs(0,[],0)
        return res

            