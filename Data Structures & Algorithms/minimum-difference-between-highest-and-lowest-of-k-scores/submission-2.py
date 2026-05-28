class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()        
        best = float('inf')
        
        for i in range(k,len(nums)+1):
            mini = nums[i-1] - nums[i-k]
            best = min(best,mini)
    
        return best
        