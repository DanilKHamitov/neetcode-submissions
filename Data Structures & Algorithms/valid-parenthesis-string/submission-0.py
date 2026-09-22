class Solution:

  def checkValidString(self, s: str) -> bool:
    leftMin = 0
    leftMax = 0

    for char in s:
      if char == '(':
        leftMin += 1
        leftMax += 1
      elif char == ')':
        leftMin -= 1
        leftMax -= 1
      else:  # Если это звездочка '*'
        leftMin -= 1  # Считаем, что она ')'
        leftMax += 1  # Считаем, что она '('

      # Если максимум ушел в минус — у нас перебор закрывающих скобок, ложь
      if leftMax < 0:
        return False

      # Минимум не может быть меньше нуля (меньше 0 открытых скобок не бывает)
      if leftMin < 0:
        leftMin = 0

    # В конце минимальный баланс должен быть ровно 0
    return leftMin == 0
