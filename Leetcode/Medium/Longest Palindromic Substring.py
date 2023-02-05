from shlex import join


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = compare_1 = compare_2 = ""
        
        for start in range(len(s)):
            for j in range(len(s[start:])):
                compare_1 = s[start:start+j+1]
                compare_2 = s[start+j:start-1 if start > 0 else None:-1]
                if len(compare_1) == 0 or len(compare_2) == 0 or compare_1[0] != compare_2[0]:
                    continue
                elif compare_1 == compare_2:
                    if len(compare_1) > len(longest):
                        longest = compare_1
        
        return longest

    def longestPalindromeEfficient(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
 
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

print(Solution().longestPalindrome("Test"))
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("abcdsbab"))
print(Solution().longestPalindrome("abababsbab"))

print(Solution().longestPalindromeEfficient("Test"))
print(Solution().longestPalindromeEfficient("babad"))
print(Solution().longestPalindromeEfficient("cbbd"))
print(Solution().longestPalindromeEfficient("abcdsbab"))
print(Solution().longestPalindromeEfficient("abababsbab"))