class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_positions = (n + 1) // 2 
        odd_positions = n // 2 
        
        MOD = 1_000_000_007

        pow5 = pow(5, even_positions, MOD)
        
        pow4 = pow(4, odd_positions, MOD)
        
        # Combine results modulo MOD
        result = (pow5 * pow4) % MOD
        
        return result


if __name__ == "__main__":
    s = Solution()
    # print(s.countGoodNumbers(1))  # Output: 5
    # print(s.countGoodNumbers(4))  # Output: 400
    print(s.countGoodNumbers(50))  # Output: 564908303
    # print(s.countGoodNumbers(1000000000))  # Output: 999999993

