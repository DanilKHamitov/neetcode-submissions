class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)        
        mx  = max(counts.values())
        cnt_mx = sum(1 for freq in counts.values() if freq == mx)
        
        print(mx,cnt_mx)
        return max((mx-1 )* (n+1) + cnt_mx,len(tasks))
        
        
         
