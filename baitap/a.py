import os
f = open("a.txt","r")
dem = 0
while True:
    a = f.readline()

    if a == "":
        break
    print("----"+a)
