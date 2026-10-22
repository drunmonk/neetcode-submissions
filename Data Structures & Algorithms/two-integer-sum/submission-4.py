class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        interm_dict={}

        for i in range(len(nums)):
            t=target-nums[i]
            if t in interm_dict:
                return [interm_dict[t],i]
            if nums[i] not in interm_dict:
                interm_dict[nums[i]]=i