class Solution:
    def countHomogenous(self, s: str) -> int:
        counter = 1
        last_charactor = s[0]
        output = 1

        for c in s[1:]:
            if last_charactor == c:
                output += counter + 1
                counter += 1
            else:
                last_charactor = c
                counter = 1
                output += counter

        return output % (pow(10, 9) + 7)
