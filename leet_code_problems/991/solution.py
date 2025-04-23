class Solution:
    operation = 0
    def brokenCalc(self, startValue: int, target: int) -> int:
        while startValue < target:
            self.operation += 1

            if target % 2 == 0:
                target = target // 2
            else:
                target += 1
        return self.operation + startValue - target