#            x        x        x
fruits = ["Apple","Orange","Banana"]

#for every x in range
for x in fruits:
    print(x)

#Can execute code when the loop is done
fruits = ["Apple","Orange","Banana"]

#for every x in range
for x in fruits:
    print(x)
else:
    print("No More Fruits")

#Break Keyword
fruits = ["Apple","Orange","Banana"]

#for every x in range
for x in fruits:
    print(x)
    break
else:
    print("No More Fruits")

#Conditional Statement inside For Loop
fruits = ["Apple","Orange","Banana","Avocado","Watermelon"]

#for every x in range
for x in fruits:
    print(x)
    if x == "Banana":
        print("Found it!")
        break
else:
    print("No More Fruits")

#-------------------------------------------------------
numbers = [1,2,3,4,5,6,7,8,9,10]

#EVEN NUMBER IS DIVISIBLE BY 2 = REMAINDER = 0
#ODD NUMBER IS NOT DIVISIBLE BY 2 = REMAINDER != 0
#MODULO %


for number in numbers:
    if number % 2 == 0:
        print(number, "Even Number")
    else:
        print(number, "Odd Number")

#Range in For Loop
for numbers in range(6):
   print(numbers)

#-----------------------------
for x in range(5):
    print("Hello World")

#ACTIVITY
#MY OUTPUT
accountUser = ["irvin","kristel","imbing"]
accountPass = ["irvinpass","kristelpass","imbingpass"]

username = input("Username: ")
password = input("Password: ")

for username in accountUser:
    if username == "irvin" and password == "irvinpass":
        print("Welcome", username)
        break
    elif username == "kristel" and password == "kristelpass":
        print("Welcome", username)
        break
    elif username == "imbing" and password == "imbingpass":
        print("Welcome", username)
        break
else:
    print("Account not Found")

#SDPT OUTPUT
accountUser = ["irvin","kristel","imbing"]
accountPass = ["irvinpass","kristelpass","imbingpass"]

username = input("Username: ")
password = input("Password: ")

for x in range(len(accountUser)):
    if username == accountUser[x] and password == accountPass[x]:
        print("Welcome", username)
        break
   
else:
    print("Account not Found")

