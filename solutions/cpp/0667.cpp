class Solution {
 public:
  vector<int> constructArray(int n, int k) {
    vector<int> ans(n);

    for (int i = 1; i < n - k; i++) ans[i - 1] = i;

    int i = n - k - 1;
    for (int j = 0; j <= k; j++)
      ans[i++] = (j % 2 == 0) ? (n - k + j / 2) : (n - j / 2);

    return ans;
  }
};