#include<bits/stdc++.h>

using namespace std;


map<int, map<int, int>> each_pos_map;

int solve(int len1, int len2, string input1, string input2) {
    int gmax_times = 0;
    int gmax_pos = 0;
    int array[len1][len2];
    for (int i = 0; i < len1; i++) {
	    //cout<<"Running external "<<i<<endl;
	    for (int j=0; j<len2; j++) {
		//cout<<"Running internal "<<j<<endl;
		if (input1[i] == input2[j]) {
		    int max_times = 1;
		    if (i!=0) {
			if (input1[i-1] == input2[j-1]) {
			    max_times = array[i-1][j-1] + 1;
			}
		    }
		    gmax_times = max(gmax_times, max_times);
		    array[i][j] = max_times;
	        }
	    }
    }
//    cout<<"Max position is "<<gmax_pos << "  "<<gmax_times<<"   "<<input1.substr(gmax_pos- gmax_times + 1, gmax_times)<<endl;
   return gmax_times;
}

int main() {
    int testcases;
    int len1, len2;
    string input1,input2;
    cin>>testcases;
    for (int i=0; i< testcases; i++) {
	cin>>len1>>len2>>input1>>input2;
	int output;
	if (len1 > len2) {
	    output = solve(len2, len1, input2, input1);
	} else {
	    output = solve(len1, len2, input1, input2);
	}
	cout<<output<<endl;
    }
}
