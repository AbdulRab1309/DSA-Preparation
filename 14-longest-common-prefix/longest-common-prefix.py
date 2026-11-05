class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs == None or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            s = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != s:
                    return strs[0][0:i]
        return strs[0]