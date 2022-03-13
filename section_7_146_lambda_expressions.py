my_list = [1, 3, 5, 7]

print(
    list(map(lambda item: item**2, my_list))
)

a = [(0, 2), (4, 3), (10, -1), (9, 9)]

print(
    sorted(list(map(lambda item: sorted(item), a)))
)
# I didn't understand at first we needed to sort
# by the second item, so this was my solution.
# the correct solution is below:

a.sort(key=lambda x: x[1])
print(a)
