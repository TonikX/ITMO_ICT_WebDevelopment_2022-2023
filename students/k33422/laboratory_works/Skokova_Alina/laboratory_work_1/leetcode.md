
# Решение задач с LeetCode для допуска к защите ЛР1

## Single Number

Given a **non-empty** array of integers `nums`, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

    Input: nums = [2,2,1]
    Output: 1

**Example 2:**

    Input: nums = [4,1,2,1,2]
    Output: 4

**Example 3:**

    Input: nums = [1]
    Output: 1
 
**Constraints:**

* `1 <= nums.length <= 3 * 104`
* `-3 * 104 <= nums[i] <= 3 * 104`
* Each element in the array appears twice except for one element which appears only once.

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in set(nums):
            repeat = nums.count(i)
            if repeat == 1:
                return i
```

## Reverse String

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

**Example 1:**

    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

**Example 2:**

    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
 
**Constraints:**

* `1 <= s.length <= 105`
* `s[i]` is a printable ascii character.

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            old = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = old
```

## Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

**Example 1:**

    Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

**Example 3:**

    Input: nums = [3,3], target = 6
    Output: [0,1]
 
**Constraints:**

* `2 <= nums.length <= 104`
* `-109 <= nums[i] <= 109`
* `-109 <= target <= 109`
* Only one valid answer exists.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        else:
            for i in range(len(nums)-1):
                diff = target - nums[i]
                if diff in nums[i+1:]:
                    diff_idx = nums[i+1:].index(diff) + i + 1
                    return [i, diff_idx]
```