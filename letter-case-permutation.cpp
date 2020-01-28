class Solution {
public:
    vector<string> answer;
    void backt(string S, int begin) {
        if (begin == S.size()) {
            answer.push_back(S);
        } else {
            if (isalpha(S[begin])) {
                S[begin] = toupper(S[begin]);
                backt(S, begin+1);
                S[begin] = tolower(S[begin]);
                backt(S, begin+1);
                
            } else {
                backt(S, begin+1);
            }
            
        }
        
    }
    vector<string> letterCasePermutation(string S) {
        backt(S, 0);
        return answer;
        
    }
};
