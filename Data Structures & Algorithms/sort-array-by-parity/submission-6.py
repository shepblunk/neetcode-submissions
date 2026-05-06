class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j = 0,len(nums)-1

        while i<j:
            num_l = nums[i]
            num_r = nums[j]
            if num_l%2 != 0 and num_r%2 == 0:
                nums[i],nums[j] = nums[j],nums[i]
                j-=1
                i+=1
            elif num_l%2 ==0 and num_r%2 == 0:
                i+=1
            else:
                j-=1
            
        return nums



        