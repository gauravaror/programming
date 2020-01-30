typedef pair<char,int> pci;
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char,int> char_freq;
        auto cmp = [](pci left, pci right) {return left.second < right.second;};
        priority_queue<pci, vector<pci>, decltype(cmp)> hi(cmp);
        for (auto i : s) {
            if (char_freq.find(i) != char_freq.end()) {
                char_freq[i] += 1;
            } else {
                char_freq.insert({i,1});
            }
        }
        for (auto i: char_freq) {
            hi.push(make_pair(i.first, i.second));
        }
        string answer;
        while (hi.size() > 0) {
            auto lem = hi.top();
            //cout<<" hkj "<<lem.first<<"  "<<lem.second<<endl;
            for (int i = 0 ; i < lem.second; i++) 
                 answer += lem.first;
            hi.pop();
        }

        return answer;
    }
};
