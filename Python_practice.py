print("Hello World")
type(3)

#How many votes did you get?
#my_votes = int(input("How many votes did you get in the election?"))
#Total votes in the election
#total_votes = int(input("What is the total votes in the election?"))
#Calculate the percentage of votes you receive
#percentage_votes = (my_votes / total_votes)*100
#print("I received " + str(percentage_votes)+"% of the total votes")

#IF-ELSE STATEMENT
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#IndexError: list index out of range
#if counties[3] != 'Jefferson':
#    print(counties[2])

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
#    print("Turn on the AC.")
#else:
#    print("Open the windows.")

"""
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
"""
"""
if "Arapahoe" in counties:
    print("True") 
else: 
    print("False")

if "El Paso" not in counties: 
    print("True") 
else: 
    print("False")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

x = 5
y = 5

if x == 5 and y == 5:
    print("True")
else:
    print("False")

if x == 3 or y == 5:
    print("True")
else:
    print("False")

if not(x > y):
    print("True")
else:
    print("False")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

"""


#REPETITION STATEMENT
"""
#while loop
x = 0
while x <= 5:
    print(x)
    x = x + 1
#infinite loop: If you forget to write code inside the loop that makes the test condition false, the while loop will continue to run

#for loop
#the county variable is declared and set equal to the first item in the list of counties, "Arapahoe."
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

#range
for num in range(5):
    print(num)

#Indexing can also be used to iterate through a list
for i in range(len(counties)):
    print(counties[i])

#Iterate through a dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#key
for county in counties_dict:
    print(county)

#key
for county in counties_dict.keys():
    print(county)

#values
for voters in counties_dict.values():
    print(voters)

#values
for county in counties_dict:
    print(counties_dict[county])

#values
for county in counties_dict:
    print(counties_dict.get(county))

#Get the Key-Value Pairs of a Dictionary
#for key, value in dictionary_name.items():
#    print(key, value)

for county, voters in counties_dict.items():
    print(county, voters)


#When iterating over a dictionary:
#The first variable declared in the for loop is assigned to the keys.
#The second variable is assigned to the values.

for county, voters in counties_dict.items():
    print(str(county) + "county has " + str(voters) + " registered")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#Get Each Dictionary in a List of Dictionaries
for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

#Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#How would you retrieve the number of registered voters from each dictionary?
for county_dict in voting_data:
     print(county_dict['registered_voters'])

#If we only want to print the county name from each dictionary, we can use county_dict['county']
for county_dict in voting_data:
    print(county_dict['county'])
"""

#Printing Formats
"""
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)
"""
