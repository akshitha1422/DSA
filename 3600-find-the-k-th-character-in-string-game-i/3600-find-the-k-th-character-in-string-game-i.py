class Solution:
    def kthCharacter(self, k: int) -> str:
        s='a'
        while len(s)<k:
            new=''
            for i in s:
                new+=chr(ord(i)+1)
            s+=new
        return s[k-1]