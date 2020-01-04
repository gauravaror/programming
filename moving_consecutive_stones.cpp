#include<bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i=a; i<=b; i++)
typedef vector<int> vi;
typedef long long ll;

class Solution {
public:
    vector<int> numMovesStonesII(vector<int>& stones) {
        int minn = INT_MAX;
        int maxn = INT_MIN;
        int total_elems = stones.size();
        map<int, int> position_stones;
        for (int i =0; i <stones.size(); i++) {
            if (stones[i] > maxn) {
                maxn = stones[i];
            }
            if (stones[i] < minn) {
                minn = stones[i];
            }
            position_stones[stones[i]] = i;
        }
        vector<int> gaps;
	int gap_near_minimum = 0;
	int gap_near_maximum = 0;
	int current_window_gap = 0;
	int min_gap = INT_MAX;
	int max_gap = INT_MIN;
	bool no_gaps = true;
        for (int i = minn; (i + total_elems -1) <= maxn; i++) {
	    if (i == minn) {
		for (int j = minn; j < minn + total_elems; j++) {
		    if (position_stones.find(j) == position_stones.end()) {
			no_gaps = false;
			++current_window_gap;
		    }
		}
	    } else {
		if (position_stones.find(i-1) == position_stones.end()) {
		    no_gaps = false;
		    --current_window_gap;
		}
		if (position_stones.find(i + total_elems-1) == position_stones.end()) {
		    no_gaps = false;
		    ++current_window_gap;
		}
	    }
	    int current_window_gap_c = current_window_gap;
	    if ((( position_stones.find(i) == position_stones.end()) || position_stones.find(i+total_elems-1) == position_stones.end()) && (current_window_gap == 1)) {
                current_window_gap_c = 2;
            }
	    cout<<"Current window at "<<i<<"  gaps "<<current_window_gap<<"  considered "<<current_window_gap_c<<endl;
	    if (max_gap < current_window_gap) max_gap = current_window_gap_c;
	    if (min_gap > current_window_gap) min_gap = current_window_gap_c;
            if (position_stones.find(i) == position_stones.end()) {
                gaps.push_back(i);
		if (i < (minn + total_elems)) {
		    ++gap_near_minimum;
		}
		if (i > (maxn - total_elems)) {
		    ++gap_near_maximum;
		}
            }
        }
	if (no_gaps) {
	    min_gap = 0;
	    max_gap = 0;
	}
	int max_moves = max(gap_near_maximum, gap_near_minimum);
        return {min_gap, max_gap};
    }
};


int main() {
    Solution sol = Solution();
    vi input = {7,4,9};
    vi input1 = {6,5,4,3,10};
    vi input2 = {100,101,104,102,103};
    vi output = sol.numMovesStonesII(input);
    cout<<output[0]<<" "<<output[1]<<endl;
    output = sol.numMovesStonesII(input1);
    cout<<output[0]<<" "<<output[1]<<endl;
    output = sol.numMovesStonesII(input2);
    cout<<output[0]<<" "<<output[1]<<endl;
    return 0;
}
