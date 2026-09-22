


class Solution:

  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
      return False

    count = Counter(hand)
    sorted_keys = sorted(count.keys())

    for k in sorted_keys:
      
      if count[k] > 0:
        start_count = count[k] 

       
        for i in range(groupSize):
          card = k + i
          if count[card] < start_count:
            return False
          count[card] -= start_count

    return True



        

             