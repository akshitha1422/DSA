class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        builder=set()
        longest=''
        for word in words:
            if len(word)==1 or word[:-1] in builder:
                builder.add(word)
                if len(word)>len(longest):
                    longest=word
        return longest