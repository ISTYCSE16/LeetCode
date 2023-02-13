class Solution {
public:
    int countOdds(int low, int high) {
        
        int count = 0;
        
        if (low % 2 == 1)
        {
            if (high % 2 == 1)
            {
                count += 2;
                low++;
                high--;
            }
            else
            {
                count += 1;
                low++;
            }
        }
        else
        {
            if (high % 2 == 1)
            {
                count += 1;
                high--;
            }
            else
            {
                count = 0;
            }
        }
        
        int ans = high - low;
        ans = ans / 2;
        
        return count + ans;
        
        
    }
};