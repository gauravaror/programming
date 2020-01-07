#include<bits/stdc++.h>
#include <cassert>
using namespace std;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i=a; i<=b; i++)
typedef vector<int> vi;
typedef long long ll;

struct pair_hash {
    template <class T1, class T2>
    std::size_t operator() (const std::pair<T1, T2> &pair) const
    {
            return std::hash<T1>()(pair.first) ^ std::hash<T2>()(pair.second);
    }
};
typedef unordered_map<pair<int,int>, unordered_map<int, int>, pair_hash> di;


class NumMatrix {
public:
    di stored_cols_sums;
    di stored_rows_sums;
    vector<vector<int>> given_matrix;
    NumMatrix(vector<vector<int>>& matrix) {
        given_matrix = matrix;
        int num_rows = matrix.size();
        if (num_rows == 0) return;
        int num_cols = matrix[0].size();
        if (num_cols == 0) return;
        int length = 2;
        while (length < num_cols) {
            int start = 0;
            for (int i = 0; i < num_rows; i++) {
                while (start + length < num_cols) {
                    int this_sum = 0;
                    for (int j = start; j< start+length; j++) {
                        this_sum += given_matrix[i][j];
                    }
                    stored_cols_sums[MP(i, length)][start] = this_sum;
                    cout<<"Cols "<<i<<"  "<<length<<"  "<<"  "<<start<<"   "<<stored_cols_sums[MP(i, length)][start]<<endl;
                    start = start + length;
                }
                start = 0;
                cout<<"I finishi "<<i<<num_rows<<endl;
            }
            length = length*2;
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        cout<<"Sum Region"<<endl;
        int slen_col = 1;
        while ((col1 % (slen_col*2)) == 0) {
            if ((col1 + slen_col*2) > col2) break;
            slen_col = slen_col*2;
        }
        int sum = 0;
        int cl1 = col1;
        int slen_col1 = slen_col;
        for (int i = row1; i <= row2; i++) {
            while (cl1 <= col2) {
                cout<<cl1<<"  "<<col2<<endl;
                if ((cl1 + slen_col) <= (col2 + 1)) {
                    if (slen_col == 1) {
                        sum += given_matrix[i][cl1];
                    } else {
                        sum += stored_cols_sums[MP(i, slen_col)][cl1];
                    }
                    cout<<"Adding sum for "<<i<<"  "<<slen_col<<"  "<<cl1<<"  "<<sum<<endl;
                    cl1 = cl1 + slen_col;
                } else {
                    if (slen_col == 1) break;
                    slen_col = slen_col /2;
                }
            }
            cl1 = col1;
            slen_col = slen_col1;
        }
        return sum;

    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */

int main() {
    vector<vi> matrix = {{3, 0, 1, 4, 2},{5, 6, 3, 2, 1},{1, 2, 0, 1, 5}, {4, 1, 0, 1, 7}, {1, 0, 3, 0, 5}};
    NumMatrix* obj = new NumMatrix(matrix);
    cout<<obj->sumRegion(2, 1, 4, 3)<<endl;
    cout<<obj->sumRegion(1, 1, 2, 2)<<endl;
    cout<<obj->sumRegion(1, 2, 2, 4)<<endl;
}
