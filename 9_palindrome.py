class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
       
        a = x
        y = 0

        while a:
            y = 10 * y + a % 10
            a /= 10
        return x == y