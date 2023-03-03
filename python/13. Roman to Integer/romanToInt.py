class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for i, c in enumerate(s):
            if i > 0 and roman_to_int[c] > roman_to_int[s[i - 1]]:
                result += roman_to_int[c] - 2 * roman_to_int[s[i - 1]]
            else:
                result += roman_to_int[c]
        return result
