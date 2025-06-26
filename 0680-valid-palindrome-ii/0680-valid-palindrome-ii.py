class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(sub):
            return sub==sub[::-1]
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return is_pal(s[i+1:j+1]) or is_pal(s[i:j])
        return True