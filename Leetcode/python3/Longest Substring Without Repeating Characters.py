# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        count = 0
        for i in s: # go through each character.
            if i in res: # check if the character is already present in res[]
                res = res[res.index(i) + 1:]# if yes then skip the previous already present character and add new repeating character at end of list.
            res.append(i) # add new or repeating character
            count = max(count,len(res)) # gets updated every iteration finally the max substring length is stored in count
        return count 
