#MWANGI ERICK
#18.02.2026
#program to show lists in python

friends = ["Shiko","Shiru","Melissa","Angel","Hope"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)

friends.append("Rose")
print(friends)

new_friends = ["Ann","Montez","Mitchell","Mwalo","Njeri"]
print(len(new_friends))

#new list of students
students = friends + new_friends
print(students)

students.pop()
print(students)

students.insert(4,"mark")
print(students)
students.insert(3,"Valaire")
print(students)

students.extend("Dan")
print(students)

students.remove("mark")
print(students)


