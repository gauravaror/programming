#include<bits/stdc++.h>
#include <math.h>
using namespace std;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i=a; i<=b; i++)
typedef vector<int> vi;
typedef vector<vector<int>> vii;
typedef long long ll;

#include<bits/stdc++.h>
#include <math.h>
using namespace std;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i=a; i<=b; i++)
typedef vector<int> vi;
typedef vector<vector<int>> vii;
typedef long long ll;

class Solution {
public:
    vector<int> bin_access(vi elem, int num) {
        int len = elem.size();
        vi cur_elem;
        int itr = len;
        for (int i = 1<<(len-1); i >= 1; i /= 2) {
            if (i&num) {
                cur_elem.PB(elem[len-itr]);
            }
            --itr;
        }
        return cur_elem;
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ss;
        const long unsigned int len = nums.size();
        for (int i = pow(2, len); i < pow(2, len+1); i++) {
            ss.PB(bin_access(nums, i));
        }
        return ss;
    }
};

int main() {
    Solution sol = Solution();
    vi aa = {1,2,3};
    auto ans = sol.subsets(aa);
    for (auto i:ans) {
	for (auto j: i) {
	    cout<<j<<"  ";
	}
	cout<<endl;
    }
}
