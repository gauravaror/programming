class Solution {
public:
    int find_ends(vector<int>& nums, int target, int start, int end, bool st) {
        int mid = (start + end)/2;
        cout<<"S"<<start<<"E"<<end<<"M"<<mid<<endl;
        while (start < end) {
            
            if (nums[mid] == target) {
                if (st) {
                    end =  mid-1;
                } else {
                    start = mid + 1;
                }
            } else {
                if (st) {
                    start = mid+1;
                } else {
                    end = mid - 1;
                }
            }
            mid = (start + end)/2;
        }
        if (st) {
            if (nums[start] == target) { 
                return start;
            } else {
                int i = 1;
                while(nums[start+i] != target) { ++i;}
                return start+i;
            return start;
        } else {
            if (nums[start] == target) return start;
            return start -1;
        }
        return start;
    }
    
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        int mid = (start + end)/2;
        while ( start < end) {
            if (nums[mid] == target) {
                int first = find_ends(nums, target, start, mid, true);
                int second = find_ends(nums, target, mid, end, false);
                return {first, second};
            } else if (nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
            mid = (start + end)/2;
        }
        if (nums.size() == 1  and nums[0] == target)
            return {0,0};
        if (start == end and nums[start] == target)
            return {start, start};
        return {-1,-1};
    }
};
