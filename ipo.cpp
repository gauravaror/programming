#define pii pair<int,int>
class Solution {
public:
    int findMaximizedCapital(int k, int W, vector<int>& Profits, vector<int>& Capital) {
        auto comp_profit = [](pii lhs, pii rhs) { return lhs.first < rhs.first;};
        auto comp_capital = [](pii lhs, pii rhs) { return lhs.second > rhs.second;};
        priority_queue<int, vector<pair<int,int>>, decltype(comp_profit)> lo(comp_profit);
        priority_queue<int, vector<pair<int,int>>, decltype(comp_capital)> hi(comp_capital);
        int len = Profits.size();
        cout<<"Ti len"<<len<<endl;
        for (int i = 0; i < len; i++) {
            if (Capital[i] <= W) {
                lo.push(make_pair(Profits[i], Capital[i]));
            } else {
                hi.push(make_pair(Profits[i], Capital[i]));
            }
        }
        
        while (k > 0) {
            cout<<" k "<<lo.size()<<"  "<<hi.size()<<"  "<<k<<endl;
            if (lo.size() == 0) break;
            pii elem = lo.top();
            lo.pop();
            W += elem.first;
            k -= 1;
            cout<<"New k"<<W<<endl;
            while (hi.size()> 0 && hi.top().second <= W) {
                pii el = hi.top();
                cout<<" dfds "<<el.first<<endl;
                lo.push(el);
                hi.pop();
            }
        }
        return W;
    }
};
