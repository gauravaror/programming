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
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        auto nextState = [](vector<int>& cells) {
            vector<int> new_state = cells;
            for (int i=0; i <cells.size(); i++) {
                if (i==0) {
                    new_state[i] = 0;
                } else if (i == (cells.size() -1)) {
                    new_state[i] = 0;
                } else if (cells[i-1] == cells[i+1]) {
                    new_state[i] = 1;
                } else {
                    new_state[i] = 0;
                }
            }
            return new_state;
        };

        auto stringify = [](vector<int> cells){

            string curr_state;
            for (int i=0; i < cells.size(); i++) {
                curr_state += to_string(cells[i]);
            }
            return curr_state;
        };

	vector<int> state = cells;
	map<string, int> state_tracker;
	int total_times = N;
        while (N > 0) {
	    string input_state = stringify(state);
	    cout<<"Current state at "<<N<<"  "<<input_state<<endl;
	    if (state_tracker.find(input_state) == state_tracker.end()) {
		state_tracker[input_state] = N;
	    } else {
		int last_occurance = state_tracker[input_state];
		int cycle = last_occurance - N;
		int cycle_rem = N % cycle;
		N = cycle_rem;
		//cout<<"Cycle"<<cycle<<" N  "<<N<<" cycle_rem "<<cycle_rem<<"  updated N "<<N-(cycle*cycle_rem)<<endl;
		//N = N - cycle*cycle_rem;
	    }
	    if (N>=1) {
	    	N--;
            	state =  nextState(state);
	    }
        }
	return state;
    }
};

int main() {
    Solution sol = Solution();
    vi prisonState = {0,1,0,1,1,0,0,1};
    sol.prisonAfterNDays(prisonState, 7);
    vi prisonState2 = {1,0,0,1,0,0,1,0};
    sol.prisonAfterNDays(prisonState2, 1000000000);
    return 0;
}
