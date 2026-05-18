class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0,len(nums)-1

        while left<=right:
            mid = (left+right)//2
            print('mid',mid)

            if left == right:
                return left

            if nums[mid]>nums[mid+1]:
                print('on compare',nums[mid],nums[mid+1])
                right = mid

            if nums[mid]<nums[mid+1]:
                print('on compare',nums[mid],nums[mid+1])
                left = mid+1
                
            print('l,r',left,right)
        return 0 