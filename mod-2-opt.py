import string

Characters = "A" + string.ascii_uppercase + string.digits + "_"

List = [268,413,438,313,426,337,272,188,392,338,77,332,139,113,92,239,247,120,419,72,295,190,131]

flag = ""

for items in List:

    remainder = pow(items, -1, 41)

    flag += Characters[remainder]


print("picoCTF{" + flag + "}")