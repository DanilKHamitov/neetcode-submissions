class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(),piles.end());
        int m = piles[piles.size()-1];
    

   
    
   int l = 1;
        int r = m;
        
        while(l < r) {  
            int mid = l + (r - l) / 2;  
            long long hr = 0;  
            
            for(int c : piles) {
                hr += (c + mid - 1) / mid;
            }
            
            if(hr > h) {
                l = mid + 1;  
            } else {
                r = mid;      
            }
        }
        
        return l;
    }
};
