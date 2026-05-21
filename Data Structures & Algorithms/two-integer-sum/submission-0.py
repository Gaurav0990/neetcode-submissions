class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i,_ in enumerate(nums):
            
            diff = target - nums[i]
            if diff in my_dict:
                return [my_dict[diff],i]
            else:
                my_dict[nums[i]] = i