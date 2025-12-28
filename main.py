class Person:
    def __init__(self,privateVar):
        self.__privateVar=privateVar
    def display(self):
        print(self.__privateVar)
    def __hello():
        print("hello")
v=Person("Ashleyna")
v.display()
v.__hello()