class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        starters = []
        

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i] , 0) + 1
        #print(hashmap)

        for num in nums:
            if num-1 not in hashmap:
                starters.append(num)
        #print(starters)
        longest = 0
        for num in starters:
            #print("on prend",num)
            current = 0
            i = 0
            while num+i in hashmap:
                current += 1
                if current>longest:
                    longest = current
                i += 1

        return longest
                




        return 0
        