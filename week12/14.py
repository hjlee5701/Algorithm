class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = min(strs, key=len)
        res = []

        common = [0] * len(prefix)
        for i in range(0, len(prefix)):
            for word in strs:
                if word[i] == prefix[i]:
                    common[i] = 1
                else:
                    common[i] = 0
                    break

        for idx in range(0, len(prefix)):
            if common[idx] == 0:
                break
            res.append(prefix[idx])

        return "".join(res)