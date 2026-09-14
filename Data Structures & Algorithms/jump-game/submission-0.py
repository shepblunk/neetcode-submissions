class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        count = 1
        goal = size-1
        for R in range(size-2,-1,-1):
            print(nums[R])
            if nums[R]>=count:
                goal = R
                count = 0
            count += 1


        return goal == 0
        
        