
# Problem: Merge Sorted Array
# Platform: LeetCode
# Difficulty: Easy
# Approach: Array Manipulation
# Time Complexity: O((m + n) log(m + n))
# Space Complexity: O(1) auxiliary space

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """
        nums1[m:] = nums2
        nums1.sort()
