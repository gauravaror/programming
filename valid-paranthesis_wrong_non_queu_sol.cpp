class Solution {
public:
    bool isValid(string s) {
        int c_o, s_o, r_o = 0;
        for (auto i:s) {
            if (i == '(') ++r_o;
            else if (i == '{') ++c_o;
            else if (i == '[') ++s_o;
            else if (i == ')') {
                if (r_o == 0) return false;
                --r_o;
            } else if (i == '}') {
                if (c_o == 0) return false;
                --c_o;
            } else if (i == ']') {
                if (s_o == 0) return false;
                --s_o;
            }
        }
        if (c_o ==0  and  s_o ==0 and r_o ==0) return true;
        return false;
    }
};
