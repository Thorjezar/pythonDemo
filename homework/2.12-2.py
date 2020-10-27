# coding=utf-8
i = 0
while i <= 9:
    j = 1
    if i <= 5:
        while j <= i:
            print("* ",end=" ")
            j += 1
        print("\n")
    else:
        j = 1
        while j <= 10 - i:
            print("* ", end=" ")
            j += 1
        print("\n")
    i += 1
