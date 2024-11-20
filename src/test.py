class A:
    def call(self):
        print("A")



class B:
    def call(self):
        print("B")


class C:
    def call(self):
        print(10**100)





def call_smt(obj):
    obj.call()



call_smt(A())
call_smt(C())
call_smt(B())