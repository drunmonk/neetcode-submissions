class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(2):
            for j in nums:
                result.append(j)
        return result
        