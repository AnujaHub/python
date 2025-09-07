
def evenOdd(x):
    if(x%2==0):
        return"even"
    else:
        return"odd"

print(evenOdd(4))    
print(evenOdd(3))    


# Types of function arguments

# default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

# keyword argument
def student(fname, lname):
    print(fname, lname)

student(fname='abc', lname='pqr')
student(lname='gfh', fname='tuv')

#Arbitrary Keyword  Arguments
# *argv packs all extra arguments into a tuple
def myFun(*argv):
    for arg in argv:
        print(arg)
myFun('hello', 'welcome', 'hi', 'lalallala')


# Variable length keyword arguments
# **kwargs collects all extra keyword arguments into a dictionary.
# kwargs.items() gives each (key, value) pair.

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun(first='abc', mid='pqr', last='tuv')

