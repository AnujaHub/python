# docstrings 

# def greet():
#     """
#     This function prints a greeting message.
#     """
#     print("Hello, World!")

# print(greet.__doc__)


# function arguments --> arbitary keyword arguments 

# non-keyword:
# def myFun(*argv):
#     for arg in argv:
#         print(arg)

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# # keyword
# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))

# myFun(first='Geeks', mid='for', last='Geeks')

# def f1():
#     s='lalallalaa'
#     def f2():
#         print(s)

#     f2()
# f1()      


# swapping nos

# def swap(x,y):
#     x,y=y,x
#     print(x,y)  

# x=10 
# y=20
# swap(x,y)
# print(x,y)    


# recursive function 

def sum(n):
    if (n==0):
        return 0
    else:
        return(n+sum(n-1))        

print(sum(5))

# rev = int(str(n)[::-1])   # converts to string, reverses, back to int



