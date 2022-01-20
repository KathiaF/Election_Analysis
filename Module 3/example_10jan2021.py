"""
name = "You"
country = "Mexico"
age = 34
hourly_way = 15
satisfied = True
daily_wage = hourly_way * 8

print(name + " live in " + country)
print(name + " are " + str(age) + " years old")
print(f"{name} make {daily_wage} per day")
print(f"Are {name} satisfied with your courrent wage? {satisfied}")
"""

"""
grocery_list = ["Milk","Bread","Eggs", "Peanut Butter", "Jelly"]
print(grocery_list)
##grocery_list.pop(3)
grocery_list.insert(3, "almond butter")
print(grocery_list)
grocery_list.remove("Peanut Butter")
#grocery_list.pop(4)
print(grocery_list)
grocery_list.pop(4)
print(grocery_list)
grocery_list.append("coffee")
print(grocery_list)
"""

pet_info = {
    "name": "Cala",
    "age": 7,
    "hobbies": ["barking", "fetching", "sleeping"],
    "wake-up-time": {
        "Mon": 8,
        "Tus": 9,
        "Wed": 9,
        "Thu": 10,
        "Fri": 11,
        "Sat": 7,
        "Sun": 6
    }
    
}

print(f'Hello my name is {pet_info["name"]}')
print(f'I am {pet_info["age"]} years old')
print(f'One of my hobbies is {pet_info["hobbies"][1]}')
print(f'On Sunday I wake up at {pet_info["wake-up-time"]["Sun"]}')
print(f'One of my hobbies is {pet_info["hobbies"][1]} and {pet_info["hobbies"][2]}')