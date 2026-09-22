class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a1 = False
        a2 = False
        a3 = False
        for a,b,c in triplets:
            if a > target[0] or b > target[1] or  c > target[2]:
                continue
            if a == target[0] :
                a1 = True
            if b == target[1] :
                a2 = True
            if c == target[2] :
                a3 = True
        return a1 and a2 and a3 
           