class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l =0;
        int r = heights.size()-1;
        int mx=0;
        while(l<r) {
            int wat  = (r-l) * min(heights[r],heights[l]);
             mx = max(wat,mx);
            if (min(heights[r],heights[l]) == heights[r] ) {
                --r;
            } else {
                ++l;
            }
        }
        return mx;
    }
};
