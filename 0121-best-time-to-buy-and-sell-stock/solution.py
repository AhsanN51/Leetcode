class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            if price<min_price:
                min_price=price
            curprofit=price - min_price
            if curprofit>max_profit:
                max_profit=curprofit
        return max_profit
