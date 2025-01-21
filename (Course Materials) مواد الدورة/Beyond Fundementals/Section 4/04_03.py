import re
phrase = "ahmed 281 years old and mohamed 30 years old and sara is 1 years old"
print(re.sub("(ahmed|mohamed) \d*", "ahmed", phrase, 1))