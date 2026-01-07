# 1) ფუნქცია არის კოდის ბლოკი რომელიც ასრულებს ამოცანას და შეიძლება ბევრჯერ გამოვიყენოთ სხვადასხვა ნაწილში.
# მაგალითად:

def funqcia(name):
    return f"hello {name}"
print(funqcia("world"))

# 2)

def test():
    print("nebismieri winadadeba")
# აქამდე ტერმინალში არაფერი გამოიტანა რადგან მხოლოდ ფუნქცია შევქმენით, მაგრამ ჯერ არ გამოგვიძახებია.
test()
test()
test()

# 3)

def sashualo_aritmetikuli():
    numbers = []
    for i in range(5):
        num = float(input("sheiyvane ricxvi: "))
        numbers.append(num)
    sashv = sum(numbers) / len(numbers)
    print("ricxvebis sashualo aritmetikulia: ", sashv)
sashualo_aritmetikuli()

# 4)

def sayHi():
    print("hello saba")
result = sayHi()
print(result)
# ფუნქციამ sayHi() ბეჭდავს ტექსტს "hello saba", მაგრამ ის არაფერს აბრუნებს, ამიტომ ავტომატურად ბრუნდება None.