class parent:
    def fun1(self):
        print("from parent")

class child(parent):
    def fun2(self):
        print("from child")
#object
obj=child()
obj.fun2()
obj.fun1()
