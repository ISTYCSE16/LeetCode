class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector <int> ans = {};
        map <int, int> numTrack;
        for (int i = 1; i <= nums.size(); ++i)
        {
            numTrack[nums[i - 1]] = i;
        }
        for (int i = 0; i < nums.size(); ++i)
        {
            if (numTrack[target - nums[i]] > 0 && numTrack[target - nums[i]] != i + 1)
            {
                int ind = numTrack[target - nums[i]];
                ans.push_back(i);
                ans.push_back(ind - 1);
                break;
            }
        }
        return ans;
    }
};