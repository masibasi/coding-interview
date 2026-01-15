# https://leetcode.com/problems/most-common-word/
# 819-most-common-word


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = ["!", "?", "'", ",", ";", "."]

        for replace_symbol in symbols:
            paragraph = paragraph.replace(replace_symbol, " ")

        count = defaultdict(int)
        paragraph = paragraph.lower().split()

        for word in paragraph:
            if word in banned:
                continue
            count[word] += 1

        max_freq = 0
        max_word = None
        for word, freq in count.items():
            if max_freq < freq:
                max_freq = freq
                max_word = word

        return max_word
