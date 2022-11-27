class Solution:
    def isPalindrome(self, x: int) -> bool:
        keep = x
        if x < 0:
            return False
        else:
            ulta = 0
            val = 1
            while val == 1:
                add = int(x % 10)
                ulta += add
                if (int(x / 10) == 0):
                    break
                ulta *= 10
                x = int(x / 10)
            if keep == ulta:
                return True
            else:
                return False