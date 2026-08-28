class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable={}
        result=[]
       

        for i in nums:
            hashtable[i]=hashtable.get(i,0)+1
        
        buket=[[] for _ in range(len(nums) + 1)] 

        for num, freq in hashtable.items():
            buket[freq].append(num) 
        

        for i in range(len(buket)-1,0,-1):
            result.extend(buket[i])
            if len(result)>=k:
                return result[:k]

        

        