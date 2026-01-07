def test():
    print("this is test function")
    name = "saba"
    print(name)

    number1 = 5
    number2 = 10

    print(number1 + number2)

test()

# -------------------------------------

def say_hi(name, ): # definition line
    if name == "saba":
        return "saba"
    else:
        return "other"

text = say_hi("saba") # saba
text = say_hi("luka") # other

print(text)