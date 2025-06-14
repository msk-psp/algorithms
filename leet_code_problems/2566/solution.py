# Today's problem.

class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = str(num)

        for index, digit in enumerate(digits):
            if digit == "9":
                continue
            else:
                break

        maximized = int(digits.replace(digit, "9"))

        miminized = int(digits.replace(digits[0], "0"))

        return maximized - miminized

    
if __name__ == "__main__":
    print(Solution().minMaxDifference(11891) == 99009)
    print(Solution().minMaxDifference(90) == 99)