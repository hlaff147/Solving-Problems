class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_number = 0
        original_number = x
        if x < 0:
            return False
        while x != 0:
            digit = x % 10
            reversed_number = (reversed_number * 10) + digit
            x = x // 10
        return original_number == reversed_number
