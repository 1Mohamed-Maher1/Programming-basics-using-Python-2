name = input("What's you name? ")
age = input("How old are you? ")
country = input("Where do you live? ")
job = input("What's your job'? ")
result = "Welcome " + name
result += ". Your age is " + age 
result += ". You live at " + country
result += ". You work as " + job
print(result)
result = f"Welcome {name}. Your age is {age}. You live at {country}. You work as {job}"
print(result)