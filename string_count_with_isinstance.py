# Write a string_count function to count how many of a list's elements are strings (the str type)

def string_count(the_list):
  total = 0
  for i in the_list:
    if isinstance(i , str):
      total += 1
  return total