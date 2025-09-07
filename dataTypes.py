a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j #not i 
print(type(c))


# sequence Data Types

# stringssss
s = 'Welcome to the Geeks World'
print(type(s))

#list
a = ["hey", "1", "yo"]
print("Accessing element from the list")
print(a[0])
print(a[1])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-2])
print(a[-3])

#tuple
#strings jaise hi just immutable - not modified once created 

tup1 = tuple([1, 2, 3, 4, 5])

# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])


# initializing empty set
s1 = set()

s1 = set("lallalallaa")
print("Set with the use of String: ", s1)
# unique elements , order doesn't matter
s2 = set(["lalla", "lall", "aa"])
print("Set with the use of List: ", s2)
