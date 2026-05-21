class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)

        l = 0
        r = len(nums) - 1

        my_list = []

        while l < len(nums):
            if l >0 and nums[l] == nums[l-1]:
                l += 1
                continue


            m = l + 1
            r = len(nums) - 1
            while m < r:
                sum = nums[l] + nums[m] + nums[r]
                if sum < 0:
                    m += 1
                elif sum > 0:
                    r -= 1
                elif sum == 0:
                    my_list.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m-1]:
                        m += 1
                    while m < r and nums[r] == nums[r+1]:
                        r -= 1   
                
            l += 1
                    
        return my_list

