## Gian Carlo

# 1. Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

print("QUESTION 1")

def hello_name(user_name):
    print(f"hello_{user_name}")

# for testing
hello_name("USERNAME")

print("\n")

# 2. Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

print("QUESTION 2")

def first_odds():
    counter = 0
    while counter < 100:
        counter += 1
        if counter % 2 == 1:
            print(counter, end=" ")

# for testing
first_odds()

print("\n")

# 3. Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

print("QUESTION 3")

def max_num_in_list(given_list):
    given_list.sort(reverse=True)
    return given_list[0]

# for testing
sample_list1 = [22, 34, 223, 94, 662, 82]
sample_list2 = [-277, 40, 7222, -85225, 87, 100]

print(max_num_in_list(sample_list1))
print(max_num_in_list(sample_list2))

print("\n")

# 4. Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

print("QUESTION 4")

def leap_year(input_year):
    if input_year % 4 == 0:
        if input_year % 100 == 0:
            if input_year % 400 == 0:
                return True
            return False
        return True
    return False

# for testing

print(leap_year(82))
print(leap_year(1900))
print(leap_year(400))
print(leap_year(100))
print(leap_year(300))
print(leap_year(104))
print(leap_year(1200))
print(leap_year(800))
print(leap_year(23))

print("\n")

# 5. Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.


print("QUESTION 5")

def consecutive_list(input_list):
    no_items = len(input_list)
    for idx in range(no_items):
        if not idx == no_items - 1:  
            if not input_list[idx + 1] - input_list[idx] == 1:
                return False
            continue
        return True
          
# for testing

print(consecutive_list([1, 3, 5, 7, 9]))
print(consecutive_list([1, 2, 3, 4, 5]))
print(consecutive_list([-1, 0, 1, 2, 3]))
print(consecutive_list([-1, 0, 1, 2, 9]))
