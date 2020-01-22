class MedianFinder {
public:

    priority_queue<int> lo;
    priority_queue<int, vector<int>, greater<int>> hi;
    
    void addNum(int num) {
        lo.push(num);
        hi.push(lo.top());
        lo.pop();
        if (lo.size() < hi.size()) {
            lo.push(hi.top());
            hi.pop();
        }
    }
    
    double findMedian() {
        cout<<lo.size()<<  "  "<<hi.size()<<"   "<<lo.top()<<"  "<<hi.top()<<endl;
        if (lo.size() > hi.size()) {
            return (double) lo.top();
        } else {
            return (double)((hi.top() + lo.top())/2.0);
        }
        
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
