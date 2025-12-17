 #Task1
#from a given string to indeces
sentence="python is amazing"
result_string=sentence[::2]
print(result_string)

#Task2
#replacing all spaces of string with underscores print the modified string
sentence="python is fun and powerful"
modified_string=sentence.title()
result=modified_string.replace(" ","_")
print(f"modified_string: {result}")

#Task3
#string s check the string contain only digits
numbers="12345"
is_digit=numbers.isdigit()
print(is_digit)

#task4
#string s print the reverse order
string="python is amazing"
reversed_string=string[::-1]
print(reversed_string)

#Task5
#given a string s captalize each first letter in the string.
string="python programming is fun"
modified_string=string.title()
print(f"modified string: {modified_string}")