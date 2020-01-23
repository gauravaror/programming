class MedianFinder {
public:
    /** initialize your data structure here. */
    multiset<int> array;
    multiset<int>::iterator lo_median, hi_median;
    
    void addNum(int num) {
        int n = array.size();
        array.insert(num);
        if (!n) {
            lo_median = hi_median = array.begin();
        } else if ( n & 1) {
            if (num < *lo_median) {
                --lo_median;
            } else {
                ++hi_median;
            }
        } else {
            if (num < *lo_median) {
                --hi_median;
            } else if (num < *hi_median) {
                ++lo_median;
                --hi_median;
            } else {
                ++lo_median;
            }
        }

    }
    
    double findMedian() {
      cout<<*lo_median<<"  hi  "<<*hi_median<<endl;
      return (*lo_median + *hi_median) /2.0;
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
