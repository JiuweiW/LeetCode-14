# C++ Naming Convention

## Return Value

```cpp
return ans;
```

```cpp
return {};
```

## Data Structures

```cpp
unordered_map<char, int> map;
vector<int> map; // even if you use array or vector, stick to map
unordered_set<string> set;
queue<TreeNode*> queue;
deque<TreeNode*> deque;
stack<char> stack;
priority_queue<ListNode*, vector<ListNode*>, compareListNode> pq;
```

```python
dict = {}
dict = collections.defaultdict(int)
dict = collections.defaultdict(list)
_set = set()
queue = collections.deque([root])
deque = collections.deque([root])
stack = []
```

## Two Pointers / Sliding Windows

Always prefer to _one_ character to represent index variables.

```cpp
int j = 0;
for (int i = 0; i < n; i++) { ... }
```

```cpp
int l = 0;
int r = nums.size() - 1;
```

## Binary Search

1. Always prefer to _one_ character to represent index variables.
2. Always prefer to use `[l, r)` pattern.

```cpp
int l = 0;
int r = nums.size(); // or nums.size() - 1

while (l < r) {
    int m = l + (r - l) / 2;
    if (f(m)) return m; // optional
    if (g(m))
        l = m + 1;      // new range [m + 1, r)
    else
        r = m;          // new range [l, m)
}

return l;    // nums[l]
```

## ListNode

```cpp
ListNode* dummy = new ListNode(NULL);

ListNode* curr;
ListNode* prev;
ListNode* next;

ListNode* slow;
ListNode* fast;

ListNode* head;
ListNode* tail;

ListNode* l1;
ListNode* l2;
```

## 2D Array / 2 Strings

```cpp
const int m = matrix.size();
const int n = matrix[0].size();

const int m = str1.length();
const int n = str2.length();

const int n = str.length(); // if there's only a string
```

## String Traversing

```cpp
for (const char& c : str) {
    doThinsWith(c);
}
```

## Boundary Check

```cpp
if (str.empty()) { ... }
if (str.length() <= 2) { ... }
```

## Boolean Variables

Always prefer to use _camelCase_ naming.

```cpp
bool isValid;
bool isNegative;
```

## Others

1. Always prefer to use `str.length()` over `str.size()`.
2. Always use _camelCase_ nomenclature when not listed above.

   For example:

   ```cpp
   int currNum;
   TreeNode* currNode;
   int maxProfit;
   ```

3. When there's confliction in expression and function:

   For example:

   - [C++]: `min`, `max` and `std::min`, `std::max`
   - [Python]: `_min`, `_max` and `min`, `max`

4. When there's confliction with default reserved words:

   - [Python]: `set` -> `_set`

5. When we need to count something, using `sum` > `count` > `total`.

6. Initialize with `0` or `false` **implicitly**

7. If there are two maps/stacks, use `1` and `2` suffixes.

    ```cpp
    unordered_map<char, int> map1;
    unordered_map<char, int> map2;
    ```

## Template

```cpp
class Solution {
public:
   // public function (only one)
   func() {
       // boundary conditions

       // init variables

       // kernel

       // return
   }

private:
   // private variables

   // private function(s)
   helper() {}

   dfs() {}
};
```
