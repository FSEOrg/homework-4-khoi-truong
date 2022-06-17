"""
Problem: https://leetcode.com/problems/valid-anagram/
"""
from typing import Dict


class Solution:
    """
    Given two strings s and t, return true if t is an anagram of s, and false \
    otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a \
    different word or phrase, typically using all the original letters exactly \
    once.

    Example 1:
        Input: s = "anagram", t = "nagaram"
        Output: true

    Example 2:
        Input: s = "rat", t = "car"
        Output: false

    Constraints:
        1 <= s.length, t.length <= 5 * 104
        s and t consist of lowercase English letters.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Idea:
            Count all character frequency and put into a dict, then compare 2 \
            dicts. 2 strings are anagram if 2 dicts is equal.
        Time complexity:
            O(max(len(s), len(t))).
        Space complexity:
            O(len(s) + len(t)). Worst case is no character duplicates in s and \
            t.
        """
        return _get_char_freq(s) == _get_char_freq(t)


def _get_char_freq(string: str) -> Dict[str, int]:
    freq = {}
    for character in string:
        if character not in freq:
            freq[character] = 1
        else:
            freq[character] += 1
    return freq
