class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      max_p=0
      i=0
      j=1
      while j < len(prices):
        if prices[i]<prices[j]:
            p=prices[j]-prices[i]
            max_p=max(max_p,p)
        else:
            i=j
        j+=1
      return max_p