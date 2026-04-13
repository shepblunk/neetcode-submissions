class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1
        while l<=r:
            m = (l+r)//2
            print(nums[m])
            if nums[m] == target:
                return m
            elif nums[m]<target:
                l = m+1
            else:
                r = m-1
        print('m',m)
        if nums[m]<target:
            return m+1
        else:
            return max(0,m)
            

        