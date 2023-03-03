class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split the string into a list of words
        words = s.split()
        # get the last word in the list
        last_word = words[-1]
        # return the length of the last word
        return len(last_word)
