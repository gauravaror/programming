#include <bits/stdc++.h>
using namespace std;
struct val{
	int first;
	int second;
};
int maxChainLen(struct val p[],int n);
int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		val p[n];
		for(int i=0;i<n;i++)
		{
			cin>>p[i].first>>p[i].second;
		}
		
		cout<<maxChainLen(p,n)<<endl;
	}
	return 0;
}
bool comparator(val a, val b) {
    if (a.first < b.first) return true;
    return false;
}

/*You are required to complete this method*/
int maxChainLen(struct val p[],int n)
{
    sort(p, (p+n), comparator);
    //Your code here
    int* maxchain = (int *) malloc(sizeof(int)*n);
    for (int i=0; i<n; i++) 
        maxchain[i] = 1;
    for (int i=1; i<n ;i++) {
        for (int j=0; j<i; j++) {
    	    //cout<<p[j].second<<"  "<<p[i].first<<endl;
            if ((p[j].second < (p[i]).first) && (maxchain[i]  < maxchain[j] + 1)) {
		//cout<<"Updating max chane at "<<i<<" "<<maxchain[i]<<"  "<<maxchain[j] + 1<<endl;
                maxchain[i] = maxchain[j] + 1;
            }
        }
    }
    int max = 0;
    for (int i =0; i < n; i++) 
        if (maxchain[i] > max) 
            max = maxchain[i];
    free(maxchain);
    return max;
    
}
