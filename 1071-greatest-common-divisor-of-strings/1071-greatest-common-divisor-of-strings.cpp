class Solution {
public:
    
    bool valid(string str1, string str2, int k)
    {
        int len1 = str1.length();
        int len2 = str2.length();
        
        if (len1 % k > 0 || len2 % k > 0) return false;
        else
        {
            string base = str1.substr(0, k);
            int n1 = len1 / k;
            int n2 = len2 / k;
            return str1 == addStr(base, n1) && str2 == addStr(base, n2);
        }
    }
    
    string addStr(string str, int n)
    {
        string ans = "";
        for (int i = 0 ; i < n ; ++i)
        {
            ans += str;
        }
        return ans;
    }
    
    string gcdOfStrings(string str1, string str2) {
        
        int len1 = str1.length();
        int len2 = str2.length();
        
        for (int i = min(len1, len2) ; i >= 1 ; --i)
        {
            if (valid(str1, str2, i)) return str1.substr(0, i);
        }
        
        return "";
        
    }
};