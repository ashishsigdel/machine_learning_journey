class Student:
    def __init__(self, name, password):
        self.name = name
        self.__password = password
    def resetPassword(self):
        print("old password is:", self.__password)


s1 = Student("Ashish", "abcd")
print(s1.resetPassword())