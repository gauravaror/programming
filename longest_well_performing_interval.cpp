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
    int longestWPI(vector<int>& hours) {
        int max_interval = 0;
        int j=0;
	int days=0;
        map<int, int> prefixes;
        while(j < hours.size()) {
            if (hours[j] > 8) {
                ++days;
            } else{ 
                --days;
            }
	    cout<<" j "<<j<<days<<endl;
            if (days > 0) {
                max_interval = j+1;
            }
            
            if (prefixes.find(days-1) != prefixes.end()) {
                max_interval = max(j-prefixes[days-1], max_interval);
            }
            
            if (prefixes.find(days) == prefixes.end()) {
                prefixes[days] = j;
            }
            j++;
            
        }
        return max_interval;
    }
};

int main() {
    Solution sol = Solution();
    vi input = {9,9,6,0,6,6,9};
    cout<<sol.longestWPI(input)<<endl;
}
