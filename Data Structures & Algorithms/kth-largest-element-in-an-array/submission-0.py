class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        interm_=[]
        for i in nums:
            interm_.append(-i)
        heapq.heapify(interm_)

        for _ in range (k):
            g=heapq.heappop(interm_)
        
        return -(g)

