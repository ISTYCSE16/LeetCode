class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel = ['a', 'e', 'i', 'o', 'u']
        vowel_count = 0
        maxi = 0
        
        for i, c in enumerate(s):
            if c in vowel:
                maxi += 1
            if i >= k and s[i - k] in vowel:
                maxi -= 1
            vowel_count = max(vowel_count, maxi)
                
        return vowel_count
        