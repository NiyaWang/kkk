grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_abs = sorted(students)
print(students_abs)

#grades_new = sum(grades[0])
#print(type(grades_new))
#grades_neww = sum(grades[0])/len(grades[0])
#print(grades_neww)

grades_new = (sum(grades[0])/len(grades[0])), (sum(grades[1])/len(grades[1])), (sum(grades[2])/len(grades[2])), (sum(grades[3])/len(grades[3])), (sum(grades[4])/len(grades[4]))
print(grades_new)
dict_marks = dict(zip(students_abs, grades_new))
print(dict_marks)