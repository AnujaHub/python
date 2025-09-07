age = int (input())
is_happy = True
if age <= 12:
    if is_happy:
      print("kiddo")
elif age <= 19:
    print("teen")
elif age <= 35:
    print("young adult")
else:
    print("adult")


# ternaray operation
s = "Adult" if age >= 18 else "Minor"
print(s)


# ( switch ) match cases 

number = 10

match number:
    case 1:
        print("ONE")
    case 2 | 3:
        print("TWO or THREE")
    case _:
        print("Other number")     # This is the "default"