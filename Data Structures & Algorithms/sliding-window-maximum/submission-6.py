class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L = 0
        somme = 0
        liste = []
        size = len(nums)
        R = k
        max_initial = max(nums[L:R])

        while R<size+1:
            number_in = nums[R-1]
            number_out = nums[L]
            max_new = max(nums[L:R])
            liste.append(max_new)
            
            L+=1
            R+=1
            

        return liste
        