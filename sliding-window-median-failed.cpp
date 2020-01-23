class Solution {
    multiset<int> array;
    multiset<int>::iterator lo_median, hi_median;
    
    void addNum(int num) {
        cout<<"Add "<<num<<endl;
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
        cout<<" After adding find "<<num<<" lo "<<*lo_median<<" hi "<<*hi_median<<endl;

    }
    
    void removeNum(int num) {
        cout<<"Remove "<<num<<endl;
        cout<<" Before Removing find "<<" lo "<<*lo_median<<" hi "<<*hi_median<<endl;
        multiset<int>::iterator elem = array.find(num);
        int n = array.size();
        if ( n % 2  == 0) {
            if (num < *lo_median) {
                ++lo_median;
            } else if ( elem == lo_median) {
                ++lo_median;
                
            } else if (elem == hi_median) {
                --hi_median;
                
            } else {
                --hi_median;
            }
        } else {
            if (lo_median == elem) {
                cout<<"Removing entering equal odd"<<endl;
                --lo_median;
                ++hi_median;
            } else if (num < *lo_median) {
                ++hi_median;
            } else if (num > *lo_median) {
                --lo_median;
            } else {
                ++hi_median;
            }
        }
        
        cout<<"Removing find "<<*elem<<" lo "<<*lo_median<<" hi "<<*hi_median<<endl;
        if (elem != array.end()) {
            array.erase(elem);
            
        }        
    }

public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> sliding_medians;
        for (int i = 0; i < nums.size() - k + 1 ; i++) {
         cout<<"Doing "<<i<<" now "<<endl;
         if (i == 0) {
             for (int j = 0; j < k; j++) {
                 addNum(nums[i+j]);
             }
         } else {
             addNum(nums[i+k-1]);
             removeNum(nums[i-1]);
         }
         sliding_medians.push_back(((double)*lo_median + (double)*hi_median)/2.0);
        
        }
        return sliding_medians;
    }
};
