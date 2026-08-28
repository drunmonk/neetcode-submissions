class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_l=height[l] #0,2
        max_r=height[r] #1
        water=0 #
        while l<r:#l=1,r=-1
              if height[l]<height[r]:
                 l+=1
                 cap=max_l-height[l] 
                 water+=(cap if cap > 0 else 0)
                 max_l=max(max_l,height[l])
                 
              else:
                r-=1
                cap=max_r-height[r] 
                water+=(cap if cap > 0 else 0)
                max_r=max(max_r,height[r])
                
        return water