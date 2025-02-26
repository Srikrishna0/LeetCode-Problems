numbers = [2, 5, 6, 8, 3, 1, 8]
even = []
odd = []

while (numbers):
  temp = numbers.pop(0)
  if temp %2 == 0:
    even.append(temp)
  else:
    odd.append(temp)

[numbers,even,odd]