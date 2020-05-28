# Create three strings using three different methods. Save your result to result_string_1, result_string_2,
# result_string_3 variables

result_string_1 = "None"
result_string_2 = 'None'
result_string_3 = """None"""


# Enter a string with your name using console and save the result to result_name variable

my_name = input("Enter you name: ")
result_name = my_name


# Enter your first and  last name. Join them together with a space in
# between. Save a result in a variable result_full_name and
# save the length of the whole name in result_full_name_length variable.

first_name = "Firuz"
last_name = "Gulomamadov"
result_full_name = first_name + last_name
result_full_name_length = len(result_full_name)


# Enter the capital city of California State in lower case. Change the case to title case.
# Save the result in result_ca_capital variable
ca_capital = "Los Angeles"
result_ca_capital = str.title(ca_capital)


# Enter the name of our planet. Change the case to upper case. Save the result in
# result_planet variable
planet = "Earth"
result_planet = str.upper(planet)
