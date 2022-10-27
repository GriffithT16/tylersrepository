# TUPLE

# months_of_year = ('Janurary', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
# print(months_of_year[2])


#SET

# fruits_veggies = {"broccoli", "oranges", "peas", "apples", "squash"}
# fruits_veggies.update(["grapefruit", "grapes"])
# fruits_veggies.update(["turnip greens", "corn"])
# print(fruits_veggies)


#DICTIONARY

# user_profile = {
#     "first_name": "Tyler",
#     "last_name": "Griffith",
#     "email_address": "GriffithT16@gmail.com",
#     "phone_number": "1-334-306-8320"
# }
# print(user_profile)


# user_profile = {
#     "first_name": input('First Name: '),
#     "last_name": input('Last Name: '),
#     "email_address": input('Email: '),
#     "phone_number": input("Phone: ")
# }
# print(user_profile)


#LIST OF DICTIONARIES
# Use a list to store the dictionary of your immediate family members,
#  with each index of the list storing its own dictionary.
#   Dictionary should contain the following keys:
# First name
# Last name
# Relation to you

fam_member1 = {
    "first": "Beverly",
    "last": "Griffith",
    "relation": "Mother"
}

fam_member2 = {
    "first": "Kendall",
    "last": "Williams",
    "relation": "Sister"
}

fam_member3 = {
    "first": "Griff",
    "last": "Keith",
    "relation": "Cousin"
}

list_of_immediate_family = (fam_member1["first"], fam_member2["first"], fam_member3["first"])
fam_relation = (fam_member1["relation"], fam_member2["relation"], fam_member3["relation"])
print(" ")
print(list_of_immediate_family)
print(fam_relation)
# print(fam_member1.get("relation"))
print(" ")

