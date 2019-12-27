#include<bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i=a; i<=b; i++)
typedef vector<int> vi;
typedef long long ll;

/**
* @brief: Does the binary on vector list
*
* @param: vi param
*
* @return: int
*/
int binary_search(vi param, int key) {
    int start = 0;
    int end = param.size();
    int mid = (start + end)/2;
    while (start<=end) {
	mid = (start + end)/2;
	if (param[mid] == key) {
	    return mid;
	} else if (param[mid] < key) {
	    start = mid + 1;
	} else {
	    end = mid - 1;
	}
    }
    return mid;
}

int binary_search2(vi param, int key) {
    int index = 0;
    for (int b=(param.size()/2); b >= 1; b /= 2) {
	while (index+b < param.size() && param[index+b] <= key) {
	    index = index + b;
	}
    }
    return index;
}

int main() {

    int testcases;
    cin>>testcases;
    REP(i, 1, testcases) {
	int array_size;
	cin>>array_size;
	vi array_elems;
	REP(j, 1, array_size) {
	    int elem;
	    cin>>elem;
	    array_elems.PB(elem);
	}
	int key;
	cin>>key;
	cout<<"Element Index bs1 "<<binary_search(array_elems, key)<<endl;
	cout<<"Element Index bs2 "<<binary_search(array_elems, key)<<endl;
    }

}
