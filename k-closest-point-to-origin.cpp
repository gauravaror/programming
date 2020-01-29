struct points  { 
        vector<int> point;
        double distance;
        points (double distance, vector<int> point) 
        :distance(distance), point(point) 
        {  }
    
        bool operator<( const points& rhs) const {
            return distance < rhs.distance;
        }
    
        bool operator>(points rhs) {
            return distance > rhs.distance;
        }
    };

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points1, int K) {
        priority_queue<points> ho;
        for (auto p: points1) {
            double distance = sqrt(pow(p[0],2) + pow(p[1],2));
            points a = {distance, p};
           // cout<<" oi "<<p[0]<<"  k "<<p[1]<<"  h "<<distance<<endl;
            ho.push(a);
            while (ho.size() > K) {
                ho.pop();
            }
        }
        vector<vector<int>> answer;
        while (ho.size() > 0) {
            answer.push_back(ho.top().point);
            ho.pop();
        }
        return answer;
    }
};
