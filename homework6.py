my_dict = {'Min Yoongi': 1993, 'Park Jimin':1995, 'Kim Namjoon':1994}
print(my_dict)
print(my_dict['Min Yoongi'])
my_dict['Kim Taehyung'] = 1995 
print(my_dict)
my_dict.update({'Jeonguk':1997, 'Hoseok':1994})
print(my_dict)
my_dict.pop('Jeonguk')
print(my_dict)
print(my_dict.get('Jeonguk'))

my_set = {1, 2, 3, 3, False, "hey", False, 1}
print(my_set)
my_set.update([4,5,6])
print(my_set)
my_set.discard(False)
print(my_set)
