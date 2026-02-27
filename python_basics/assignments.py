#MWANGI ERICK
#DATE:16.02.2026
#program to calculate income tax

salary = int(input("enter your gross salary"))

if salary < 50000:
    tax =(2.5/100*(salary))
    net_salary = salary - tax

    print(f"Gross salary = (salary)")
    print(f"Tax =")