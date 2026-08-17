class Solution:
    def countSubstrings(self, s: str) -> int:
        res = ""
        reslen = 0
        cnt_palindroms =0
        for i in range(len(s)):
            #odd length
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1) > reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                cnt_palindroms+=1
                
                l-=1
                r+=1
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r-l+1) > reslen:
                    res = s[l:r+1]
                    reslen = r-l+1
                cnt_palindroms+=1
                
                l-=1
                r+=1
       
        return cnt_palindroms