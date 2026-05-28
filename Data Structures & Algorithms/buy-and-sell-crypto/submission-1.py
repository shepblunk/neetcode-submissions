class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1
        best = 0
        while right < len(prices):
            if prices[right]>prices[left]:
                profit = prices[right] - prices[left]
                best = max(profit,best)
            else:
                left  = right
            right += 1
        return best


            
        