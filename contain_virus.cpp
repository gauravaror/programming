#include<bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i=a; i<=b; i++)
typedef vector<int> vi;
typedef long long ll;

#include<bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i=a; i<=b; i++)
typedef vector<int> vi;
typedef long long ll;


class Solution {
public:
    struct pair_hash {
        template <class T1, class T2>
        std::size_t operator() (const std::pair<T1, T2> &pair) const
        {
                return std::hash<T1>()(pair.first) ^ std::hash<T2>()(pair.second);
        }
    };

    vector<pair<int,int>> actions = {{0,1,},{0,-1},{1,0},{-1,0}};
    void dfs(vector<vector<int>>& grid, unordered_set<pair<int,int>, pair_hash>& seen,
            unordered_map<int,unordered_set<pair<int,int>, pair_hash>>& cc,
            unordered_map<int, int>& perimeter,
            unordered_map<int, unordered_set<pair<int,int>, pair_hash>>& frontiers,
            int& current_component,
            int row,
            int col, 
            int num_rows,
            int num_cols) {
        if (grid[row][col] == 1) {
            if (seen.find(MP(row, col)) == seen.end()) {
                seen.insert(MP(row,col));
                cc[current_component].insert(MP(row, col));
                for (int i =0; i < 4; i++) {
                    int new_row = row + actions[i].first;
                    int new_col = col + actions[i].second;
                    if ((new_row >= 0) && (new_row < num_rows) && 
                         (new_col >= 0) && (new_col < num_cols)) {
                        //cout<<"Processing "<<new_row<<"  "<<new_col<<" grid "<<grid[new_row][new_col]<<"  "<<row<<" "<<col<<endl;
                        if (grid[new_row][new_col] == 1) {
                                //cout<<" Adding "<<new_row<<","<<new_col<<" to connected component "<<current_component<<endl; 
                                cc[current_component].insert(MP(new_row,new_col));
                                dfs(grid, seen, cc, perimeter, frontiers, current_component,
                                    new_row, new_col, num_rows, num_cols);
                        } else if (grid[new_row][new_col] == 0) {
                            //cout<<" Adding "<<new_row<<","<<new_col<<" to frontier "<<current_component<<endl; 
                            frontiers[current_component].insert(MP(new_row, new_col));
                            perimeter[current_component]++;
                        } else {

                        }
                    }
                }
            }
        }
    }

    int containVirus(vector<vector<int>>& grid) {
        int ans = 0;
        while (true) {
            int num_rows = grid.size();
            int num_cols = grid[0].size();
            unordered_set<pair<int,int>, pair_hash> seen;
            unordered_map<int, unordered_set<pair<int, int>, pair_hash>> connected_components;
            unordered_map<int, unordered_set<pair<int, int>, pair_hash>> frontiers;
            unordered_map<int, int> perimeter;
            int current_component = 0;

            //cout<<"Num Rows "<<num_rows<<" Num Cols "<<num_cols<<endl;
            for (int i= 0; i < num_rows; i++) {
                for (int j= 0; j < num_cols; j++) {
                    if (seen.find(MP(i,j)) == seen.end()) {
                            connected_components[current_component] = unordered_set<pair<int,int>, pair_hash>();
                            frontiers[current_component] = unordered_set<pair<int,int>, pair_hash>();
                            perimeter[current_component] = 0;
                            dfs(grid, seen, connected_components,
                                perimeter, frontiers, current_component, i, j,
                                num_rows, num_cols);
                            if (perimeter[current_component] != 0) current_component++;
                    }

                }
            }
            if ((current_component == 0) && (perimeter[0] == 0)) break;
            int max_perimeter = frontiers[0].size();
            int walled_cc = 0;
            for (int i = 0; i <= current_component; i++) {
               // cout<<"Current components "<<i<<"  perimenter zero "<<perimeter[i]<<"  "<<walled_cc<<endl;
                if (max_perimeter < frontiers[i].size())  {
                    max_perimeter = frontiers[i].size();
                    walled_cc = i;
                }
            }
            ans += perimeter[walled_cc];
            cout<<"Adding to ans "<< ans << " compnonent "<<walled_cc<<endl; 
            for (int i = 0; i < current_component; ++i) {
                if (i == walled_cc) {
                    for (auto reg: connected_components[i]) {
                        grid[reg.first][reg.second] = -1;
                    }
                } else {
                    for (auto reg: connected_components[i]) {
                        for (int i =0; i < 4; i++) {
                            int new_row = reg.first + actions[i].first;
                            int new_col = reg.second + actions[i].second;
                            if ((new_row >= 0) && (new_row < num_rows) && 
                                (new_col >= 0) && (new_col < num_cols)) {
                                if (grid[new_row][new_col] == 0) {
                                    grid[new_row][new_col] = 1;
                                }
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
};

int main() {
    Solution sol = Solution();
    vector<vector<int>> grid = {{1,1,1},{1,0,1},{1,1,1}};
    cout<<sol.containVirus(grid)<<endl;
    vector<vector<int>> grid1 = {{1,1,1,0,0,0,0,0,0},{1,0,1,0,1,1,1,1,1},{1,1,1,0,0,0,0,0,0}};
    cout<<sol.containVirus(grid1)<<endl;
    vector<vector<int>> grid2= {{0,1,0,0,0,0,0,1},{0,1,0,0,0,0,0,1}, {0,0,0,0,0,0,0,1}, {0,0,0,0,0,0,0,0}};
    cout<<sol.containVirus(grid2)<<endl;
}
