class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_c=0
        l=0
        r=len(heights)-1

        while l<r:
            area=(r-l)*min(heights[l],heights[r])

            if max_c < area:
                max_c=area

            inter=min(heights[l],heights[r])
            if heights[l] ==inter:
                l+=1
            else:
                r=r-1

        return max_c

               
        