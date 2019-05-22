class Solution {
 public:
  vector<string> summaryRanges(vector<int>& nums) {
    vector<string> ans;

    const int n = nums.size();
    for (int i = 0; i < n; i++) {
      int start = nums[i];
      while (i < n - 1 && nums[i] == nums[i + 1] - 1) i++;
      int end = nums[i];
      if (start == end)
        ans.push_back(to_string(start));
      else
        ans.push_back(to_string(start) + "->" + to_string(end));
    }

    return ans;
  }
};