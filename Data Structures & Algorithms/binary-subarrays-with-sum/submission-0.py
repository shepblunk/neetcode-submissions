from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def atMost(k):
            if k < 0:
                return 0
            L = 0
            somme = 0
            count = 0
            for R in range(len(nums)):
                somme += nums[R]
                while somme > k:
                    somme -= nums[L]
                    L += 1
                count += R - L + 1
            return count

        return atMost(goal) - atMost(goal - 1)