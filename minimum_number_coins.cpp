//#include<bits/stdc++.h>
#include<iostream>
#include<map>

using namespace std;

int available_denominations[10] = {2000, 500, 200, 100, 50, 20, 10, 5 , 2 ,1};

struct coins {
    map<int, int, std::greater<int>> denominations;

    int get_sum() {
	int sum = 0;
	for (auto& vk :  denominations) {
	    sum += vk.first*vk.second;
	}
	return sum;
    }

    int get_counts() {
	int sum = 0;
	//cout<<"Starting counts"<<endl;
	for (auto& kv :  denominations) {
	    //cout<<"Doing counts "<<kv.first<<"  "<<kv.second<<endl;
	    sum += kv.second;
	}
	return sum;
    }
};

map<int, coins> minimum_change_deniminations;

coins
access_denominations(int deno) {
    auto min = minimum_change_deniminations.find(deno); 
    if (min !=  minimum_change_deniminations.end()) {
	auto c = min->second;
	return c;
    }
    coins a;
    return a;
}

coins 
find_denominations(int deno) {
    //cout<<"Finding denomination "<<deno<<endl;
    coins a;
    if (deno <= 0) return a;
    coins available = access_denominations(deno);
    if (available.get_counts() != 0) return available;
    coins min;
    int min_counts = 100000000;
    for (auto i : available_denominations) {
	coins iter;
	int current_val = deno-i;
	if (current_val < 0)  continue;
	coins a = find_denominations(deno-i);
	a.denominations[i] += 1;
	if (min_counts > a.get_counts()) {
	    min = a;
	    min_counts = a.get_counts();
	}
    }
    minimum_change_deniminations.insert(pair<int, coins>(deno, min));
    return min;
}

int main() {

    int testcases, N;
    cin>>testcases;
    for (int i=0; i < testcases; i++) {
	cin>>N;
	//cout<<"Finding denominations for "<<N<<endl;
	auto ans = find_denominations(N);
	for (auto kv : ans.denominations) {
	    for (int i =0; i<kv.second; i++) {
	    	cout<<kv.first<<" ";
	    }
	}
	cout<<endl;
	//cout<<ans.get_counts();
    }
}
