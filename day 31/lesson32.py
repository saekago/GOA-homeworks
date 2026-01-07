def find_clone(text, char):
    result = -1
    index = 0

    for i in text:
        if i == char and result == -1:
            result = index
        index += 1

    print(result)

find_clone("aSaba", "a") # 0
find_clone("aSaba", "S") # 1
find_clone("aSaba", "z") # -1