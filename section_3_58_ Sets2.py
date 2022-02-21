#create a piece of code that a school principal can use to immediately find out who missed class so they can call the parents

#school's student database, is a set
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#teacher attendance is a list
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

#Students who do not attend class
misses_class = school.difference(attendance_list)

print(misses_class)