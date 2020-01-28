#define PB push_back
typedef vector<vector<int>> vvi;
typedef vector<int> vi;


class Solution {
public:
    vvi answer;
    void backtracking(vector<int> nums, vi curr_sol) {
        if (nums.size() == 0) {
            answer.PB(curr_sol);
            return;
        } else {
            for (int i = 0; i < nums.size(); i++) {
                curr_sol.PB(nums[i]);
                vi cp = vi(nums);
                cp.erase(cp.begin() + i);
                backtracking(cp, curr_sol);
                curr_sol.pop_back();
            }
        }
        
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
         backtracking(nums, {});
         return answer;        
    }
};
