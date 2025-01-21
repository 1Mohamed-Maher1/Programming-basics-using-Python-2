firstName = "abu Bakr"
lasttName = "Al-Siddiq"
title = "The Caliph of Muslims"
title = "The, Caliph, of, Muslims"

print (firstName.capitalize())
print(firstName.lower())
print(title.find("Muslims"))
print(title.replace("Muslims", "Islam"))
print(title[4:])

parts = title.split(",")
for part in parts:
    print(part.strip().capitalize())
    