class Solution {
public:
    vector<string> answer;
    void backt(string cur_para, int n, int curr_open, int curr_finished) {
        if (curr_open == 0 and curr_finished == n) {
            answer.push_back(cur_para);
        } else {
            if (curr_open > 0) {
                backt(cur_para+")", n, curr_open-1, curr_finished+1);
            }
            if (curr_open + curr_finished < n) {
                backt(cur_para+"(", n, curr_open+1, curr_finished);
            }
        }
    }
    
    vector<string> generateParenthesis(int n) {
        backt("", n, 0, 0);
        return answer;
        
    }
};
