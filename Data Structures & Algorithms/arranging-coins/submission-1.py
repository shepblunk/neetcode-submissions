class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return 1
        k=0
        i=1
        while n>i:
            n = n-i
            k +=1
            i+=1
        return k
