#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int a = 0;

        for (auto it = nums.begin(); it != nums.end(); it++) {
            cout << *it << "";
            a++;
        }

        cout << "a: "+a << "";

        return a;
    }
};

Solution s = Solution();

vector<int> nums = [1,1,2];

s.removeDuplicates(nums);