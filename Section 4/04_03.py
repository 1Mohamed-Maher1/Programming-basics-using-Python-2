import re
phrase = "ahmed 281 years old and mohamed 22 years old and sara 1 years old"
print(re.sub("(ahmed|mohamed) \d*", "ahmed", phrase, 1))

