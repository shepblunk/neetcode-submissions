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
            count_zeros = hashmap.get(0,0)
            if count_zeros > k:

                number_left = nums[L]
                hashmap[number_left] -= 1
                if hashmap[number_left] == 0:
                    del hashmap[number_left]
                
                count_zeros = hashmap.get(0,0) - 1
                L+=1

            best = max(best,R-L+1)

        return best
                
            

        