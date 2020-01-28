#include<bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i=a; i<=b; i++)
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef long long ll;

class Solution {
public:
    vvi answers;
    void backtrack_solution(vi nums, int first_elem, int sol_size, vi current_sol){
	if (current_sol.size() == sol_size) {
	    answers.PB(current_sol);
	    return;
	}
	for (int j = first_elem; j < nums.size(); j++) {
	    if (j != first_elem and nums[j] == nums[j-1]) continue;
	    current_sol.PB(nums[j]);
	    backtrack_solution(nums, j+1, sol_size, current_sol);
	    current_sol.pop_back();
	}	
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
	sort(nums.begin(), nums.end());
	for (int i = 0; i <= nums.size(); i++) {
	    backtrack_solution(nums, 0, i, {});
	}
        return answers;
    }
};

int main() {
    Solution sol = Solution();
    vi aa = {2,1,2};
    auto ans = sol.subsetsWithDup(aa);
    for (auto i:ans) {
	for (auto j: i) {
	    cout<<j<<"  ";
	}
	cout<<endl;
    }
}
