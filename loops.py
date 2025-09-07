
# # 0 to n-1
# n = 4
# for i in range(0, n):
#     print(i)
    
# li=["abc" , "pqr" , "rst"]
# for i in li:
#     print(i)

#      # or
     
# li=["abc" , "pqr" , "rst"]
# for index in range(len(li)):
#     print(li[index])    

# tup=("abc" , "pqr" , "rst")
# for i in tup:
#     print(i)    

# str = "cupcake"
# for i in str:
#     print(i)      


# i=0
# while(i!=5) :
#     i=i+1
#     print(i)

# # nested
# for letter in 'abcde':
#     if letter == 'e' or letter == 'b':
#         continue
#     print('Current Letter :', letter)


# # the loop iterates over each letter 
# # but doesn't perform any operation
# for letter in 'abcdedfg':
#     pass
# print('Last Letter :', letter)

# items = input("Enter shopping items separated by commas: ").split(',')

# for item in items:
#     print(item.strip())

    # strip removes unwanted spaces or gaps

# k=1
# n = int(input())
# for k in range(1,n+1):
#     print(k**2)


# n = int(input("enter num"))
# sq=1
# i=1

# for sq in range(1,n+1):
#     for i in range(1,11):
#          print(sq*i, end=" ")
#     print()     



# 2x2 indentity matrix pattern   

# i=1
# j=1
# for i in range(1,3):
#     for j in range(1,3):
#          if i==j:
#           print("1" , end=' ')
        
#          else:  
#           print("0" , end=' ')
#     print() 

# k = 5 
# li =[1,2,3,4,5,6,7]    

# for i in li:
#     if(i==5):
#         break
#     print(i) 

li=["a","b","c","out of stock","d"]    

for i in li:
    if(i=="out of stock"):
        continue
    print(i)