# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:

    def guessNumber(self, n: int) -> int:

        start = 1
        end   = n
        while True:
            if guess(start) == 0:
                return start
            elif guess(end) == 0:
                return end
            else:
                half = math.ceil((start + end)/2)
                if guess(half) == 0:
                    return half
                elif guess(half) == 1:
                    start = half + 1
                elif guess(half) == -1:
                    end = half - 1