class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        starters = []
        
        for num in nums:
            if num-1 not in hashset:
                starters.append(num)
        #print(starters)
        longest = 0
        for num in starters:
            #print("on prend",num)
            current = 0
            i = 0
            while num+i in hashset:
                current += 1
                if current>longest:
                    longest = current
                i += 1

        return longest
      