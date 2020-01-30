class Solution {
public:
    struct clel {
      int x;
      int distance;
      clel(int x, int distance) 
          : x(x), distance(distance) {}
      bool operator< (clel const & point) const {
          if (abs(distance) != abs(point.distance)) {
              return abs(distance) < abs(point.distance);
          } else {
              return x < point.x;
          }
      }
    };
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        priority_queue<clel> ho;
        for (auto i: arr) {
                clel el(i, i-x);
                ho.push(el);
            while(ho.size()>k) {
                ho.pop();
            }
        }
        vector<int> elems;
        while (ho.size() >0) {
            clel t = ho.top();
            elems.insert(elems.begin(),t.x);
            ho.pop();
        }
        sort(elems.begin(), elems.end());
        return elems;
        
    }
};
