class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefixe=1
        for i in range(len(nums)):
            res[i]=prefixe
            prefixe*=nums[i]
        postfixe=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfixe
            postfixe*=nums[i]
        return res


        