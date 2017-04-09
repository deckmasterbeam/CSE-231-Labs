dictionary = open("dictionary.txt", "r")
for x,y in enumerate(dictionary):
    if x == 9:
        print(x,y)