class Solution():
    def maxProfit(self, prices):
        res = 0
        for each in range(len(prices) - 1):
            if prices[each + 1] > prices[each]:
                res += (prices[each + 1] - prices[each])
        return res