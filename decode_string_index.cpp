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
    string decodeAtIndex(string S, int K) {
	string tape;
        REP(i,0, S.length()-1)
	    if (isdigit(S[i])) {
		int curr_digit = int(S[i]) - 48;
		cout<<"Tap len "<<tape.length()<<"  curr "<<curr_digit<<"  K "<<K<<endl;
		if ((tape.length()*curr_digit) > K) {
		    cout<<"Current tape"<<tape<<"  K "<<K<<"  curr_digit "<<curr_digit<<endl;
		    int index = K%tape.length() - 1;
		    if (index < 0) {
			index += tape.length();
		    }
		    string output;
		    output += tape[index];
		    cout<<"Tape char"<<tape[index]<<endl;
		    return output;
		} else {
		    string copy = tape;
		    REP(j,1,curr_digit-1)
			tape += copy;
		    cout<<"Repeated tape "<<copy<<"  "<<tape<<"  cur "<<curr_digit<<endl;
		}
	    } else {
		tape += S[i];
	    }
    }
};

int main() {
    Solution sol = Solution();
    cout<<sol.decodeAtIndex("ha22", 5)<<endl;
    cout<<sol.decodeAtIndex("a2345678999999999999999", 1)<<endl;
    cout<<sol.decodeAtIndex("leet2code3", 10)<<endl;
}
