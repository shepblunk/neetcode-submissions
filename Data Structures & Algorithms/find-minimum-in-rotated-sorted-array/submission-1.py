class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1

        while left<right:
            mid = (left+right)//2
            print(mid,'mid')
            
            print('comapre',nums[mid],nums[mid-1])
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right = mid
            print(left,right)

        return nums[left]
        