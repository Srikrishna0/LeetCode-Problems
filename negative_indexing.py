#Finish the balanced_list function below. It should decide whether a list starts and ends with the same value. Only the first and last list element matter here; the rest of the elements can be anything.

#You can solve this with a single == comparison that uses negative indexing!

#You'll also need to handle the case where the list is empty. (In that case, your function should return True.)

def balanced_list(the_list):
  if the_list == [] or the_list[0] == the_list[-1]:
    return True
  else:
    return False