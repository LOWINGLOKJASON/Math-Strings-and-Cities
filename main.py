###############################
# Wing Lok LO
# link: https://replit.com/join/meckzekhob-lowinglokjason
###############################

#Question 1 - Four programs
#Create a = 2000, b = 23 and c equals a plus b.
a = 2000
b = 23
c = a+b
print(c)

#Create a message welcome then change the first letter to upper letter of each word.
message = "welcome to"
n_message = message.title()
print(n_message)

#create a name as JOHN WICK and remove the extra space as well as in proper format.
first_name = "john "
last_name = " wicK "
full_name = f"{first_name.upper().strip()} {last_name.upper().strip()}"
print(full_name)

#Create a full message by combining the above with full name on the first line and welcome message on the second line.
full_message = f"{full_name} \n{n_message} {c}"
print(full_message)

#Question 2 - City names
#Create Hong Kong as city 1.
city_1 = "Hong Kong"
print(city_1)

#Create Toronto as city 2 and print it with the fisrt letter as upper letter.
city_2 = "toronto"
print(city_2.title())

#Create Manchester as city 3 and print it all as upper letters.
city_3 = "Manchester"
print(city_2.upper())

#Question 3: My name
#Store my name
name = "Wing Lok LO"
full_name = f"{name}"
print(full_name)

#Add a message combining my name as a sentence
first_name = "Wing Lok"
last_name = "LO"
messege = f"My name is {first_name} {last_name}."
print(messege)

#Modify name to uppercase 
messege_uppercase = f"My name is {first_name.upper()} {last_name.upper()}."
print(messege_uppercase)

#Modify name to lowercase
messege_lowercase = f"My name is {first_name.lower()} {last_name.lower()}."
print(messege_lowercase)

#Modify name to titlecase 
messege_titlecase = f"My name is {first_name.title()} {last_name.title()}."
print(messege_titlecase)

#Question 4: Calculation
#addition then change it to f string
a = 2022+1
print(a)
print(f"Adding 1 into 2022 equals {a}")

#subtraction then change it to f string
b = 2024-1
print(b)
print(f"subtracting 1 from 2024 equals {b}")

#multiplication then change it to string using a join
c = 289*7
print(c)
print("Multiplying 289 seven times equals " + str(c))

#division then change it to string using a join
d = 4046/2
print(d)
print("4046 is divided by two equals", str(d))
