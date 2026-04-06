class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        prefix_sum  = []
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                count += 1
            if sum-k in hashmap:
                count += hashmap[sum-k]
            prefix_sum.append(sum)
            hashmap[sum] = hashmap.get(sum,0) + 1
            

        #print(prefix_sum)
        #print(hashmap)

       

        return count
        