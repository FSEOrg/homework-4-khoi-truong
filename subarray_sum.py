"""
Problem: https://leetcode.com/problems/subarray-sum-equals-k/
"""
from typing import List


class Solution:
    """
    Given an array of integers nums and an integer k, return the total number \
    of subarrays whose sum equals to k.
    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:
        Input: nums = [1,1,1], k = 2
        Output: 2

    Example 2:
        Input: nums = [1,2,3], k = 3
        Output: 2
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Idea:
            Base on the prefix-sum idea, we can get sum of any sub array from \
            index i to j like this:
                sum(subarray[i -> j]) = prefix_sum(j) - prefix_sum(i)
                (with j >= i)
            Because the sum of subarray should be equal to k, the condition \
            can be converted to:
                k = prefix_sum(j) - prefix_sum(i)
                (with j >= i)
            Convert again we have:
                prefix_sum(i) = prefix_sum(j) - k
                (with j >= i)
            If we calculate the cummulative sum at each index in nums array, \
            we can calculate the remainder at that index too:
                remainder_at(i) = cummulative_sum(i) - k
            So we can use a dictionary to store the frequency of cummulative \
            sum. Then we can check whether the remainder existed in the \
            dictionary and its frequency.
        
        Time complexity:
            O(N) where N is the length of nums.
        Space complexity:
            O(N) where N is the length of nums. (worst case that there is no \
            duplicated cummulative sums)
        """
        if not nums:
            return 0
        count = 0
        sum_freq = {0: 1}
        cummulative_sum = 0
        for num in nums:
            cummulative_sum += num
            remainder_sum = cummulative_sum - k
            if remainder_sum in sum_freq:
                count += sum_freq[remainder_sum]
            sum_freq[cummulative_sum] = sum_freq.get(cummulative_sum, 0) + 1
        return count
