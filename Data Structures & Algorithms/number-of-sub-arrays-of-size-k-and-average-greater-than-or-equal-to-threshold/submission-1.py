class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = k*threshold
        current_sum = sum(arr[:k])
        count = 0

        if current_sum>=target_sum:
            count += 1
        
        for r in range(k,len(arr)):
            current_sum +=arr[r] - arr[r-k]
            if current_sum>=target_sum:
                count += 1
        

        return count
                
        