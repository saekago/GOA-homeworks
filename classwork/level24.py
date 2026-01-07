# 1)
#          0         1          2         3        4
cars = ["car I", "car II", "car III", "car IV", "car V"]

# 2)
print(cars[2])

# 3)
print(cars[3])

# 4)
names = ["nino", "giorgi", "mariami", "levani", "sofo", "daviti", "tamari"]
names[0] = "elene"
names[4] = "luka"
print(names)

# 5)
names = ["elene", "giorgi", "mariami", "levani", "luka", "daviti", "tamari"]
print(names)
names[1], names[6] = names[6], names[1]
print(names)