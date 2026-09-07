class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = 0
        best = 0
        hashmap = {}
        count_zeros = 0
        size = len(nums)
        for R in range(size):
            number_right = nums[R]
            hashmap[number_right] = hashmap.get(number_right,0)+1
            #print(hashmap)
            count_zeros = R-L+1 - sum(nums[L:R+1])
            #print("zeros",count_zeros)
            while count_zeros > k:
                #print(f" on dépasse k")
                number_left = nums[L]
                #print("number left",number_left)
                hashmap[number_left] -= 1
                #print(f"new hashmap",hashmap)
                if hashmap[number_left] == 0:
                    del hashmap[number_left]
                L+=1
                count_zeros = R-L+1 - sum(nums[L:R+1])

            best = max(best,R-L+1)

        return best
                
            

        