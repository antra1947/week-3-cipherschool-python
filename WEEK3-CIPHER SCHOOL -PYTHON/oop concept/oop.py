object
a=5
isinstance(a,object)

a + 4
print(a+4)


class A:
    pass
type(A)
print(type)



a = 4
def func():
    pass
print(type(func))

def say_hi(self):
    print(self.name)
    self.name="anonymous"

    class Person:
        name = "Antra"
        say_hi = say_hi


    p = Person()
    p.say_hi()

class A:
 name= "Antra" 
 marks=30
print(type(A))

class A:
    def _call_(self):
        print("You called me")
        a = A()
        print(type(a))


        class Exponent:
            def _init_(self,n):
                self.n = n

                def _getitem_(self,x):
                    return x ** self.n
                    

                class Dog:
                    kind = 'canine'
                    def _init_(self,name):
                        self.name = name
                        a = Dog("Maxx")
                        a.name
                        a.kind
                        'canine'




  