class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        res=[]
        for i,char in enumerate(s):
            hashmap[char] = i
        #print(hashmap)

        size = 0
        end = 0
        for i,char in enumerate(s):
            if char in hashmap:
                size += 1
                end=max(hashmap[char],end)

            if i==end:
                res.append(size)
                size = 0

        return res