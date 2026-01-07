# boolean (bool) - ბულიანი.
# True მნიშვნელობები: 1, 0.1, "-".
# False მნიშვნელობები: 0, 0.0, "".
print(bool(0.1))
number = int(input("enter the number (0+): "))
print(bool(number and 5 - 4)) # True
print(bool(0 and 5 - 4)) # False
# if - თუ.
# else - სხვა შემთხვევაში.
# 1) მომხმარებელს შემოვატანინოთ ასაკი.
# 2) შევამოწმოთ მისი ასაკი არის თუარა 18-ზე ნაკლები.
# 3.1) თუ 18-ზე ნაკლებია, მაშინ დავბეჭდოთ "you are kid".
# 3.2) თუ 18-ზე მეტია ან ტოლია, მაშინ დავბეჭდოთ "you are adult".
age = int(input("please enter your age: "))
# if (პირობა):
# : - კოდის ბლოკის დასაწყისი
if age >= 18:
    print("you are adult")
else:
    print("you are kid")