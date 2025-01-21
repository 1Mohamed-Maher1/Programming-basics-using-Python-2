import re
text = "almdrasa is your way to learn programming the right way. almdrasa badges motivate students to do more. almdrasa quize help students practice on what they have learned through the course. almdrasa courses are one of a kind because they were made by professionales. almdrasa look and feel is one of kind. almdrasa wishes you good learning. thanks. "
replacement = re.sub("almdrasa \w{4,}", "Almdrasa", text, 3)
print(replacement)