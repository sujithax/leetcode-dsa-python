
# Problem: Best Time to Buy and Sell Stock
# Platform: LeetCode
# Difficulty: Easy
# Approach: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_min = prices[0]
        max_profit = 0

        for price in prices:
            if price < current_min:
                current_min = price
            else:
                profit = price - current_min

                if profit > max_profit:
                    max_profit = profit

        return max_profit
