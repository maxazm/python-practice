class MyClass(object):

    def mymethod(self):
        print("this is normal method")

    @staticmethod
    def mystaticmethod():
        print("this is static method")

c = MyClass()
c.mymethod()
MyClass.mystaticmethod()
# c.mystaticmethod()