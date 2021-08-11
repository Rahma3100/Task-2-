for x in range(7):
    for y in range(5):
        if y == 0 or (y == 4 and (x != 0 and x != 3)) or ((x == 0 or x == 3) and (0 < y < 4)):
            print("* ", end="")
        else:
            print(end="  ")
    print()

