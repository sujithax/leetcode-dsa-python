
# Problem: Best Time to Buy and Sell Stock II
# Platform: LeetCode
# Difficulty: Medium
# Approach: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit = prices[i + 1] - prices[i]
                max_profit += profit

        return max_profit
