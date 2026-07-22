class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(),n = matrix[0].size();
        int bot = m-1;
        int top =0;
        while(top <= bot) {
            int row = (top + bot)/2;
            if(target > matrix[row][n-1]) {
                top = row+1;
            }
            else if (target < matrix[row][0]) {
                bot = row -1;
            } else {
                break;
            }
        }
        if(!(top <=bot)) {
            return false;
        }
        int row = (top + bot)/2;

          int l=0,r = n-1;
          while(l<=r) {
            int mid = (l+r)/2;
            if(target > matrix[row][mid]) {
                l = mid+1;
            }
            else if (target < matrix[row][mid]) {
                r = mid -1;
            }
            else {
                return true;
            }
          }  
         return false;
        
    }
};
