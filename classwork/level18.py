# 1)

number1 = int(input("enter number1: "))

if number1 < 10:
    print("number1 is less than 10")
elif number1 < 20:
    print("number1 is less than 20")

# 2)

number2 = int(input("enter number2: "))
if number2 % 2 == 0:
    print("the number2 is even.")
else:
    print("the number2 is odd.")

# 3)

weather = input("enter todays weather: ")
if weather == "sunny weather":
    print("i will train outside.")
elif weather == "rainy weather":
    print("i will train inside.")
else:
    print("i will not train today.")

# 4)

for i in range(3):
    print("saxeli")