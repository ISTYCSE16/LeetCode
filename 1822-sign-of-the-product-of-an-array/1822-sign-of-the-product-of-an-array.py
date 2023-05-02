class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0
        for each in nums:
            if each < 0:
                count += 1
            elif each == 0:
                return 0
        ans = 0
        if count % 2 == 0:
            ans = 1
        else:
            ans = -1
        return ans