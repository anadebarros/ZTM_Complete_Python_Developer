def highest_even(li):
  new_list = []
  li.sort()
  for number in li:
    if number % 2 == 0:
      new_list.append(number)
      highest_even = new_list.pop()
  return highest_even

print(highest_even([1,3,4,6,11]))
