#Task 1:Reverse List
my_list = [10,20,30,40,50,11]
reversed_list = my_list[::-1]    #reverse the list using slicing
print(reversed_list)

# Output should be: [11,50,40,30,20,10]

#Task 2:Common Elements:l
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
common_elements = [element for element in list1 if element in list2] #list comprehension to find common elements
print(common_elements)

# Output should be: [4, 5]

#Task 3:Unique Elements:
original_list = [1,2,2,3,4,4,5]  #given list
unique_list = []                 #initialize empty list for unique elements
for item in original_list:       #iterate through the original list
    if item not in unique_list:  #check if the item is not already in unique_list
        unique_list.append(item)  #add unique item to the list
        print(unique_list)

# Output should be: [1, 2, 3, 4, 5]

#Task 4:Remove Duplicates:
duplicated_list = [1,2,2,3,4,4,5]  #given list with duplicates
no_duplicates_list = []            #initialize empty list for no duplicates
for item in duplicated_list:       #iterate through the duplicated list
    if item not in no_duplicates_list: #check if the item is not already in no_duplicates_list
        no_duplicates_list.append(item)  #add unique item to the list
        print(no_duplicates_list)

# Output should be: [1, 2, 3, 4, 5]

#Exercise 1: List Concatenation
list_a = [1,2,3]
list_b = [4,5,6]
concatenated_list = list_a + list_b    #concatenate the two lists
print(concatenated_list)

# Output should be: [1, 2, 3, 4, 5, 6]

#Exercise 2: List Repetition
original_list = [7,8,9]
repeated_list = original_list * 3      #repeat the list three times
print(repeated_list)

# Output should be: [7, 8, 9, 7, 8, 9, 7, 8, 9]

#Exercise 3: List Removal
my_list = [10,20,30,40,50,60,70]
filtered_list = [my_list[i] for i in range(len(my_list)) if i%2 !=0] #list comprehension to filter out even indices
print(filtered_list)

# Output should be: [20, 40, 60]

#Exercise 4: List Insertion
my_list = [20,30,40]
numbers_to_insert = [10,11,12]
for number in reversed(numbers_to_insert):    #reverse the numbers to maintain order when inserting
    my_list.insert(0, number)                #insert each number at the beginning
    print(my_list)

# Output should be: [10, 11, 12, 20, 30, 40]


#List comprehensions
#1. Square Numbers: Create a list of squares of numbers from 1 to 10.

squares = [x**2 for x in range(1,11)]    #list comprehension to generate squares
print(squares)

# Output should be: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#2. Even Numbers: Generate a list of even numbers from 1 to 20.

even_numbers = [x for x in range(1,21) if x%2 ==0]  #list comprehension to filter even numbers
print(even_numbers)

# Output should be: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


#3. Words Lengths: Given a list of words, create a list containing the lengths of each word.
#words = ["apple", "banana", "cherry", "date"]

words = ["apple", "banana", "cherry", "date"]
word_Lengths = [len(word) for word in words]    #list comprehension to get lengths of each word
print(word_Lengths)

# Output should be: [5, 6, 6, 4]

#4. Filter Negative Numbers: From a list of numbers, create a new list that contains only the positive numbers.
numbers = [-10, 15, -20, 25, 30, -5]
positive_numbers = [num for num in numbers if num >0]  #list comprehension to filter positive numbers
print(positive_numbers)         
# Output should be: [15, 25, 30]


