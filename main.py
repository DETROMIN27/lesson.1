#Клас студента школи 
# данні студента - ім'я, прізвище, логіки, група, логін та пароль, вік, телеграм
# дії сьудента - вивод інформації
#  - загальна кількість логіків

class Student:
    def __init__ (self,name,surname, age,logiks,
            groups, login, password,telegram):
        self.name = name
        self.surname = surname
        self.age = age
        self.logiks = logiks
        self.groups = groups
        self.login = login 
        self.password = password
        self.telegram = telegram
    def all_info (self):
        print("All information of student")
        print("Name - ",self.name)
        print("Surname - ",self.surname)
        print("Age - ",self.age)
        print("Logiks - ",self.logiks)
        print("Groups - ",self.groups)
        print("Login - ",self.login)
        print("Password - ",self.password)
        print("Telegram - ",self.telegram)
    def logika_info(self):
        print("===================Logiks of students====================")
        for logik in self.logiks:
            lg += str(logik)+", "
        all_lg = sum(self.logiks)
        print(lg)
        print("All logiks:", all_lg)
        print("============================================")

studens = list()
student = Student("Dasha","Polyak",13,[7,2,8,9,10,3],"Python","ppppp","553234","@ghghg")
students.append(student)
print("======All students=======")
for i in range(len(studens)):
    print(i,"-",studens[i].surname)

while True:
    print("What do you want? 1 - all info , 2 -logics, 3 - exit")
    do = int(input(""))
    who = int(input("Enter numbers of  student"))
    if do == 1:


