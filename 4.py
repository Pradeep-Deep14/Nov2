class MyClass:
    def __init__(self,my_var):
        self.my_var=my_var

    def instance_method(self):
        self.my_var=30
        return f"{self.my_var}"

obj=MyClass(10)
obj.instance_method()

print(obj.my_var)

#30
#So, the code demonstrates the use of instance variables and methods within a class. It creates an instance of the class,
# modifies the instance variable using a method, and then prints the updated value of the variable