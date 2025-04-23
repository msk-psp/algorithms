class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # one hour == 30 degree
        # half hour == 15 degree
        hour_pin = hour % 12 * 30 + minutes % 60 * 0.5
        minute_pin = minutes / 60 * 360

        return min(max(hour_pin, minute_pin) - min(hour_pin, minute_pin), abs(max(hour_pin, minute_pin) - min(hour_pin, minute_pin) - 360))

if __name__ == "__main__":
    print(Solution().angleClock(3, 15) == 7.5)

    print(Solution().angleClock(1, 57))



