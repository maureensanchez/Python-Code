integers_list = []
print("Welcome!")
print("Please, when prompt, enter four different integers. ")
first_integer = int(input("Please enter the first integer: "))
integers_list.append(first_integer)
second_integer = int(input("Please enter the second integer: "))
integers_list.append(second_integer)
third_integer = int(input("Please enter the third integer: "))
integers_list.append(third_integer)
fourth_integer = int(input("Please input the last integer: "))
integers_list.append(fourth_integer)
print("The integers you entered are: ", integers_list)

maximum_integer = max(integers_list)
print("The maximum integer is: ", maximum_integer)

minimum_integer = min(integers_list)
print("The minimum integer is: ", minimum_integer)

count_even = 0
count_odd = 0
count_between = 0
count_positive = 0
count_negative = 0
adding_integers = 0
for integer in integers_list:
    adding_integers = adding_integers + integer
    if integer % 2 == 0:
        count_even = count_even + 1
    else :
        count_odd = count_odd + 1
    if integer > 0 and integer < 50:
        count_between = count_between + 1
    if integer < 0:
        count_negative = count_negative + 1
    else:
        count_positive = count_positive + 1

print("The number of even integers  is: ", count_even)
print("The number of odd integers are : ", count_odd)
print("The number of integers greater than 0 but less than 50: ", count_between)
print("The number of positive integers: ", count_positive)
print("The number of negative integers: ", count_negative)


average_small_and_largest = (maximum_integer + minimum_integer)/2
print("The average of the smallest and largest integers: ", average_small_and_largest)
average_all = adding_integers/4
print("The average of the four integers is : ", average_all)
