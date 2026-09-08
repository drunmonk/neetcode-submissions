class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
    
            minheap=[]
            res=[]
            for i,j in points:
                a=((i)**2 +(j)**2)**.5
                minheap.append([a,i,j])
            
            heapq.heapify(minheap)

            while k>0:
                a,i,j=heapq.heappop(minheap)
                k-=1
                res.append([i,j])
            
            return res



    
