def rotate_left(the_list):
  # TODO: Remove the first element, and put it at the end of the list.
  the_list.append(the_list.pop(0))
  return the_list

def rotate_right(the_list):
  # TODO: Remove the last element, and put it at the front of the list.
  the_list.insert(0,the_list.pop())
  return the_list

#predefined code
assert rotate_left(["a"]) == ["a"]
assert rotate_left(["a", "b"]) == ["b", "a"]
assert rotate_left(["a", "b", "c"]) == ["b", "c", "a"]

assert rotate_right(["a"]) == ["a"]
assert rotate_right(["a", "b"]) == ["b", "a"]
assert rotate_right(["a", "b", "c"]) == ["c", "a", "b"]