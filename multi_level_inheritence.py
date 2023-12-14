#base class
class Apple:  #grand parent class
    def fun1(self):
        print("from apple")

#intermidiate class
class orange(Apple):  # parent class with grand parent class
    def fun2(self):
        print("from orange")
#derived class

class banana(orange):  #  child class with parent
    def fun3(self):
        print("from banana")

#object
fruit=banana()
fruit.fun1()
fruit.fun2()
fruit.fun3()
