class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for num, _ in enumerate(s):
            if num == len(s) - 1:
                # If it's the last character, just assign its value
                roman_map[s[num]] = roman_map[s[num]]
                continue
            ch = s[num]
            next_ch = s[num + 1]
            value = roman_map[ch]
            if num < len(s) - 1 and next_ch > ch:
                # If the next character is larger, subtract the current value
                roman_map[ch] = -value
            else:
                # Otherwise, keep the value as is
                roman_map[ch] = value
        return sum(roman_map.values())


if __name__ == "__main__":
    s = "MCMXCIV"  # Example input
    solution = Solution()
    result = solution.romanToInt(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    # Output: 1994
    # Explanation: MCMXCIV = 1000 + (1000 - 100) + (100 - 10) + 5 = 1994
