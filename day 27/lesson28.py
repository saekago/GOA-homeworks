# len() - გადაეცემა ერთი არგუმენტი, ეს შეიძლება იყოს string-ი ან list-ი და აბრუნებს მის სიგრძეს (მასში ელემენტთა/სიმბოლოთა რაოდენობას).
print("-----------len()-----------")
names0 = ["giga", "goga", "saba"]
print(len(names0))

word = "hello"
print(len(word))

# .append - გადაცემა მხოლოდ ერთი არგუმენტი, რომელსაც ჩაამატებს სიის ბოლოში. ის მხოლოდ სიის ფუნქციაა და გამოიძახება dot ნოტაციით.
print("-----------.append-----------")

names1 = ["globalio", "lol", "sae"]
print(names1)

names1.append("vaska")
print(names1)

# .insert - გადაეცემა მხოლოდ ორი არგუმენტი: ინდექსი სადაც ჩაემატება ელემენტი, ელემენტი რომელიც უნდა ჩაემატოს(ანუ გვეხმარება სიის ნებისმიერ ადგილას დავამატოთ ელემენტი, რაც არ შეეძლო .append ფუნქციას).
print("-----------.insert-----------")

#          -3      -2      -1
#           0       1       2
names2 = ["gio", "luka", "davit"]
print(names2)

names2.insert(2, "jimshe")
print(names2)

# .pop - შლის სიიდან ერთ ელემენტს, გადაეცემა ერთი არგუმენტი და ეს არის ინდექსი, რომელზე მდგომ ელემენტსაც წაშლის სიაში. შეიძლება არგუმენტი არ გადაეცეს და ამ შემთხვევაში ავტომატურად სიის ბოლო ელემენტს წაშლის.
# თუ სია ცარიელია ან .pop ფუნქციას არარსებული ინდექსი გადავეცით, მისი გამოძახება შეცდომას გამოიტანს.
print("-----------.pop-----------")

#            0          1       2
#           -3         -2      -1
names3 = ["sandro", "salome", "ana"]
print(names3)

names3.pop(-1)
print(names3)

# 
print("-----------.for-----------")

numbers = []

for i in range(1, 100 + 1):
    numbers.append(i)
print(numbers)

print("----------------------")

numbers.pop()
numbers.insert(12, 100)
numbers.append("string")
print(numbers)

print(len(numbers))