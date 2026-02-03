"""
PROBLEM STATEMENT:

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

class Solution:
    def longestCommonPrefix(self, strings: list[str]) -> str:
        if not strings or "" in strings:
            return ""
        
        if len(strings) == 1:
            return strings[0]
            
        common_prefixes = []
        for iteration in range(len(strings[0])):
            char = strings[0][iteration]
            for string_idx in range(len(strings)):
                # Safety: If a word is too short or doesn't match, stop.
                if iteration == len(strings[string_idx]) or strings[string_idx][iteration] != char:
                    return "".join(common_prefixes)
            common_prefixes.append(char)
        return "".join(common_prefixes)
      