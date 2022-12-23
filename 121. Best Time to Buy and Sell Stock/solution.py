class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy_pointer = 0
        sell_pointer = 1
        max_profit = 0

        while sell_pointer < len(prices):
            
            if prices[sell_pointer] < prices[buy_pointer]:
                buy_pointer = sell_pointer
            
            current_profit = prices[sell_pointer] - prices[buy_pointer]
            max_profit = max(current_profit, max_profit)

            sell_pointer += 1

        return max_profit
