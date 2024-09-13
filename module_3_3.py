def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print("\nФункция с параметрами по умолчанию:")
print_params()
print_params(5)
print_params(5, 'текст')
print_params(5, 'текст', False)
print_params(b=25)
print_params(c=[1, 2, 3])
print("\nРаспаковка параметров из списка и словаря:")
values_list = [3.14, 'hello', True]
values_dict = {'a': 50, 'b': 'dict_', 'c': None}
print_params(*values_list)
print_params(**values_dict)
print("\nРаспаковка + отдельные параметры:")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)