#how to create a class
class student:
    #attributes
    #constructors are important for creating objects

    def __init__(self, name, age, classNO, hobby):
        self.name=name
        self.age=age
        self.classNO=classNO
        self.hobby=hobby

    #methods are functions to do something
    def display_student_info(self):
        print("The student's Details are: ")
        print("The name of the student is:", self.name)
        print("The age of the student is", self.age)
        print("Studying in class", self.classNO)
        print("Hobby is", self.hobby)

    def change_name(self):
        print("Please enter your age:")
        self.age=int(input())
        print("What is the name correction?")
        self.name=input()

#Create 2 objects
leo = student("Leo", 11, "year1", "climing wall")
tristan = student("Tristan", 9, "year9", "lego")

zachary = student("Zachary", 5, "year 4", "dancing")
dudicus = student("Dudicus", 48, "year 21", "football")

leo.display_student_info()
leo.change_name()
leo.display_student_info()

tristan.display_student_info()
tristan.change_name()
tristan.display_student_info()

zachary.display_student_info()
zachary.change_name()
zachary.display_student_info()

dudicus.display_student_info()
dudicus.change_name()
dudicus.display_student_info()