
# Problem: Majority Element
# Platform: LeetCode
# Difficulty: Easy
# Approach: Hash Map (Dictionary)
# Time Complexity: O(n) average
# Space Complexity: O(n)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = {}

        for i in range(len(nums)):
            if nums[i] not in majority:
                majority[nums[i]] = 1
            else:
                majority[nums[i]] += 1

            if majority[nums[i]] > len(nums) // 2:
                return nums[i]
