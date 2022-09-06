class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for i in range(1, n):
            size = len(nums)
            for j in range(0, size):
                t = nums.pop(0)
                if t == 0: continue
                mod = t % 10
                if (k == 0):
                    nums.append((t*10 + mod))
                    continue
                if (mod - k) >= 0:
                    nums.append((t*10 + (mod - k)))
                if (mod + k) < 10:
                    nums.append((t*10 + (mod + k)))
            
        
        return nums
                