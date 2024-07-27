immutable_var = 5, 7, 'Котики', True
# immutable_var[0] = 3
# print(immutable_var[0]) - элемент tuple не изменяется, в отличии от списка, и используется для хранения постоянных значений. при этом занимая меньше места.
mutable_list = [5, 7, 'Котики', True]
mutable_list[0] = 3
print(mutable_list)
