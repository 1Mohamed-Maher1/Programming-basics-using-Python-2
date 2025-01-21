firstName = "abu Bakr"
lastName = "Al-Siddiq"
title = "The Caliph of Muslims"
title = "The, Caliph, of, Muslims"

print(firstName.capitalize())
print(lastName.lower())
print(title.find("Muslims"))
print(title.replace("Muslims", "Islam"))
print(title[4:])

parts = title.split(",")
for part in parts:
    print(part.strip().capitalize())