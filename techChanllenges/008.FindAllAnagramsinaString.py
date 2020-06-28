# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        ls = len(s)
        lp = len(p)

        if ls < lp or lp == 0:
            return []

        wordCountP = self.getWordCount(p)
        wordCountS = self.getWordCount(s[:lp])

        diffList = self.getDiffLists(wordCountS, wordCountP)
        diffCount = self.getDiffCount(diffList)

        res = []

        if diffCount == 0:
            res.append(0)

        for i in range(ls - lp):
            # pop the first c
            oldc = s[i]
            diffList[self.getIndex(oldc)] -= 1

            # check the change of diffCount
            if diffList[self.getIndex(oldc)] == 0:
                diffCount -= 1
            if diffList[self.getIndex(oldc)] == -1:
                diffCount += 1

            # push the new c
            newc = s[i + lp]
            diffList[self.getIndex(newc)] += 1

            # check the change of diffCount
            if diffList[self.getIndex(newc)] == 0:
                diffCount -= 1
            if diffList[self.getIndex(newc)] == 1:
                diffCount += 1

            # cehck diffCount to get index if ok
            if diffCount == 0:
                res.append(i + 1)
        return res

    def getWordCount(self, l):
        counts = [0 for x in range(26)]

        for c in l:
            counts[self.getIndex(c)] += 1

        return counts

    def getIndex(self, c):
        return ord(c) - ord("a")

    def getDiffLists(self, l1, l2):
        res = [0 for x in range(26)]
        for i in range(26):
            res[i] = l1[i] - l2[i]
        return res

    def getDiffCount(self, l):
        count = 0
        for x in l:
            if x != 0:
                count += 1

        return count
