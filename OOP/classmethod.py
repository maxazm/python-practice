class MyClass(object):

    class_method_count = 0

    def mymethod(self):
        print("this is normal method from {}".format(self))

    @staticmethod
    def _mystaticmethod():
        print("this is static method")

    @classmethod
    def _myclassmethod(cls):
        cls.class_method_count += 1
        print(f"This is classmethod and now the count is {cls.class_method_count}")

c = MyClass()
c.mymethod()
MyClass.mystaticmethod()
MyClass.myclassmethod()
MyClass.myclassmethod()
# c.mystaticmethod()