class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        k=0
        nums.sort()
        MOD = 10**9 + 7 
        left,right = 0,len(nums)-1
        while left<=right:
            if nums[left]+nums[right]<=target:
                k+=2**(right-left)
                left+=1
            elif nums[left]+nums[right]>target:
                right-=1
        return k%MOD


        