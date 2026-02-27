#MWANGI ERICK
#17.02.2026
#program to illustrate break in python

number = 1
while number<10:
    print(number)
    number+=1



    if number == 4:
        print('loop has been broken')
        break # breaks numbers when it gets to 4

    if number==3:
        continue
    print(number)
