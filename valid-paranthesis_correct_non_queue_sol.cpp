#define PB push_back

class Solution {
public:
    bool isValid(string s) {
        int c_o=0;
        int s_o =0;
        int r_o = 0;
        vector<char> opened;
        for (auto i:s) {
            cout<<"iff"<<i<<endl;
            if (i == '(') {
                ++r_o;
                opened.PB('(');
            } else if (i == '{') {
                ++c_o;
                opened.PB('{');
            } else if (i == '[') {
                ++s_o;
                opened.PB('[');
            }else if (i == ')') {
                if (opened.size() == 0) return false;
                if (r_o == 0) return false;
                char t = opened.back();
                opened.pop_back();
                if (t != '(') return false;
                --r_o;
            } else if (i == '}') {
                if (opened.size() == 0) return false;
                char t = opened.back();
                opened.pop_back();
                if (t != '{') return false;
                if (c_o == 0) return false;
                --c_o;
            } else if (i == ']') {
                if (opened.size() == 0) return false;
                char t = opened.back();
                opened.pop_back();
                if (t != '[') return false;
                if (s_o == 0) return false;
                --s_o;
            }
                    cout<<"ccc"<<c_o<<" "<<s_o<<"  "<<r_o<<endl; 
        }
        cout<<"ccc"<<c_o<<" "<<s_o<<"  "<<r_o<<endl; 
        if (c_o ==0  and  s_o ==0 and r_o ==0) return true;
        return false;
    }
};
