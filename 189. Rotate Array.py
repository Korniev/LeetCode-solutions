"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
from typing import List


# Reverse the whole array
# Reverse the first k elements
# Reverse the rest of the elements
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        self.reverse(nums, 0, n - 1)

        self.reverse(nums, 0, k - 1)

        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


# Simple reverse
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        k = k % n

        rotated = [0] * n
        for i in range(n):
            rotated[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = rotated[i]


# Reverse step by step
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        for _ in range(k):
            last = nums[-1]
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = last
