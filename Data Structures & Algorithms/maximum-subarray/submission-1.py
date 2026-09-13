class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        new_l = [0]
        for R in range(len(nums)):
            new_l.append(nums[R]+new_l[-1])
            #print(new_l)

        #print(min(new_l))
        max_sum = float('-inf')
        min_prefix = new_l[0]

        for i in range(1,len(new_l)):
            max_sum = max(new_l[i]-min_prefix,max_sum)
            min_prefix = min(min_prefix,new_l[i])
    
        return max_sum


        