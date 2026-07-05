class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        size = len(nums)
        lwst = float('inf')
        sum = 0
        for R in range(size):
            new_number = nums[R]
            #print('nsw',new_number)
            sum += new_number
            #print(sum)
            while sum>=target:
                lwst = min(lwst,R-L+1)
                #print('sup')
                number_out = nums[L]
                #print('out',number_out)
                
                sum -= number_out
                L+=1
                #print(sum)
        if lwst == float('inf'):
            return 0
        return lwst
                
            
        