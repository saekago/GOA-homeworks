# range - დიაპაზონი.
# i - საიტერაციო ცვლადი.
# default values: start = 0, step = 1.
# range(end)
# range(start, end)
# range(start, end, step)
# start - რიცხვი, საიდანაც იწყება დიაპაზონი.
# end - რიცხვი, სადაც მთავრდება დიაპაზონი.
# step - განსაზღვრავს, ყოველი მერამდენე რიცხვი ავიღოთ დიაპაზონიდან.
# 1) რადგან მხოლოდ ერთი მნიშვნელობა წერია და ეს არის end, start და step იღებენ default მნიშვნელობებს. range(5) ---> 0,1,2,3,4.
# 2) რადგან მხოლოდ start და end წერია range ფუნქციის არგუმენტად, step მიიღებს default მნიშვნელობებს. range(5, 10) ---> 5,6,7,8,9.
# 3) start, end და step ცნობილია, ამიტომაც ქარხნული მნიშვნელობა არცერთს არ ექნება. range(2, 10, 2) ---> 2,4,6,8.

print("-1-")

for i in range(5):
    print(i)

print("-2-")

for i in range(5, 10):
    print(i)

print("-3.1-")

for i in range(2, 10, 2):
    print(i)

print("-3.2-")

for i in range(1, 10, 2):
    print(i)

# password incorrect repeat
print("-password-")

password = "12345678"
user_input = input("please enter your password: ")

# while ციკლი გვეხმარება რომ შევასრულოთ იტერაციები იქამდე, სანამ მისი პირობა არის ჭეშმარიტი.
while password != user_input:
    print("incorrect password!")
    user_input = input("please enter your password: ")
print("password is correct!")