print("python 14 homework")
class Student:
    pay = 1000
    status = True

    def __init__(self, fname, lname, age, grades):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.grades = grades


    # სახელი და გვარი
    def get_full_name(self):
        return f"{self.fname} {self.lname}"


    # ფასდაკლება
    def discount(self, discount_percent):
        discount_amount = 0

        if self.age < 18:
            discount_amount = (discount_percent / 100) * self.pay
            self.pay -= discount_amount
        return self.pay


    #საშუალო ქულა
    def calculate_avarage_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return average_grade


    def get_status(self):
        average_grade = self.calculate_avarage_grade()

        if average_grade > 90:
            print("Excellent")
        elif 70 <= average_grade <= 90:
            print("Good")
        elif 70 > average_grade < 50:
            print("aberage")
        elif average_grade < 50:
            Student.status = False
            print("poor")

student1 = Student("malkhaz", "okriashvili", 22, [92, 92, 90, 89 ,81, 77, 65, 85, 97, 64, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,])
# student2 = Student("nika", "okriashvili", 13, [98, 92, 93, 89, 95, 86, 78, 96, 95])

print(student1.get_full_name())
print(student1.discount(20))
print(student1.calculate_avarage_grade())
print(student1.get_status())
print(Student.status)




