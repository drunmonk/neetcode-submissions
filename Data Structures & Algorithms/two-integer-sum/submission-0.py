class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            interm=target -nums[i]

            if interm in d:
                return [d[interm],i]
            else:
                d[nums[i]]=i


        