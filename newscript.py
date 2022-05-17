first_name="Alex"
last_name="Santel"
birthday="26 of March 19XX"
number=42
animal="Octopus"
hobbies="playing guitar, piano and drums"
course="Applied Bioinformatics and Biostatistics - ABI-2022-2"

print(f"Hi. My name is {first_name} {last_name} and I was born on {birthday}. I applied for the course {course} for reorientation and to enhance my employability. My hobbies are {hobbies}. My favorite animal is probably {animal}. My lucky number is {number}. Bonus points for everyone who gets it")

print("Name:",{first_name},"Last Name:",{last_name})
print("some {0} have {1} eyes".format(animal,number))
print(f"{3*14} is the winning number")
print(f"{first_name.lower()} is my name written with lowercase capital")
print({first_name,last_name})
print("this is just a text string")
print("I have to get 14 of these")
print("we try it oldschool here with %%-formatting. Like in  %s. I am %s." %(birthday,first_name))
print("Hello, {}. I am {}.".format(animal,first_name))
print(f"We are all in the course {course}.")
print(f"{hobbies}  can get boring at times. practicing can be tiring. So it is important to take breaks.")
print("This will hopefully be the last print")
print("{}{} is done.".format(first_name,last_name))
print(f"practicing {hobbies} with f-strings means something different depending on what you mean by strings.")
