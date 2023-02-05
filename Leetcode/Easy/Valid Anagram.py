class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:                                             # Save s in dictionary instead
            if i not in t:
                return False

            if len(t) > 0:
                t = t.replace(i, "", 1)

        for i in t:
            if i not in s:
                return False

            if len(s) > 0:
                s = s.replace(i, "", 1)
                

        return True

    def isAnagramEfficient(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}

        for i in s:
            dic1[i] = dic1.get(i, 0) + 1

        for i in t:
            dic2[i] = dic2.get(i, 0) + 1
            
        return dic1 == dic2

print(Solution().isAnagram("anagram","nagaram"))
print(Solution().isAnagram("rat","car"))
print(Solution().isAnagramEfficient("anagram","nagaram"))
print(Solution().isAnagramEfficient("rat","car"))