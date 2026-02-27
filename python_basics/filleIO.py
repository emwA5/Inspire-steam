#MWANGI ERICK
#23.02.2026
#program to perfom file operations

#create to new file
new_file = open("student_date.txt", "r+")


#write to new file
new_file.write("{student name : Erick Mwangi, ID : 28325839 email : em4020520@gmail.com}")


#read from the file
new_file = open("student_date.txt", "r+")

data = new_file.read()

print(data)

#delete file 
#use os module
import os
os.remove("remove.txt")

#delete folder
os.rmdir("folder")