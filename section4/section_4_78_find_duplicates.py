some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

empty_list = []
  
for letter in some_list:
  if some_list.count(letter) > 1:
    empty_list.append(letter)
    if empty_list.count(letter) >1:
      empty_list.remove(letter)
print (empty_list)

#if we wanted to use list function:
#single_duplicates = set(empty_list)
#print(list(single_duplicates))