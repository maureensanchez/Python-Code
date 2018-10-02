# CSC120
# Lab11Template.py
import random
import math

def fill(ax, nx, x, y):
        # Populate array ax of size = nx with random integers in the range x  y
        #
    j = 0
    while (j < nx):
      randNum = random.randint(x, y)
      ax.insert(j, randNum)
      j = j + 1
    return ax

def display(ax):
    print("2. Display the list as follows == ", ax)  # DONE


def sum_list(ax):
    s = sum(ax)
    # return the sum of the integers in the list
    #it will be used in the ave() function
    #s = 10000
    return s


def sort_list_asc(ax):
    sorted_list = sorted(ax, reverse=True)
    return sorted_list


def min_integer(ax):
    # return the smallest value in the list
    smallest = min(ax)
    return smallest


def max_integer(ax):
    # return the largest value in the list
    mx = max(ax)  # place holder only
    return mx

def avg_of_list(ax):
    # return the average of the integers in the list
    #must call the sum() function here and divide by the size of the array
    size_of_array = sum_list(ax)
    average_list = size_of_array/len(ax)
    return average_list


def evens(ax):
    count_even = 0
    for i in ax:
        if i % 2 == 0:
            count_even = count_even + 1
    return count_even


def odds(ax):
    count_odd = 0
    for i in ax:
        if i % 2 != 0:
            count_odd = count_odd + 1
    return count_odd

def digit10x(ax):
    intergers_with_one = []
    for i in ax:
        first_digit = math.floor(i/100)
        if first_digit == 1:
            intergers_with_one.append(i)
    return intergers_with_one


def n_count(ax, n):
    # return the number of times n appears in the list a
    x = ax.count(n)
    return x


# NOW we call the function

n = 25
a = 100
b = 300
myArray = []
myArray = fill (myArray,n,a,b)
display(myArray)
s = sum_list(myArray)
sorted_list = sort_list_asc(myArray)
mn = min_integer(myArray)
m = max_integer(myArray)
average = avg_of_list(myArray)
e = evens(myArray)
o = odds(myArray)
x = digit10x(myArray)


# Outputs
print("3. The sum of all the integers in the list is :", s)
print("4. The list in sorted order (largest to smallest)is :  ", sorted_list)
print("5. The minimum integer in the list  is : ", mn)
print("6. The maximum integer in the list  is: ", m)
print("7. The average of the integers in the list is : ", average)
print("8. The number of even integers is: ", e)
print("9. The number of odd integers is: ", o)
print("10. The integers in the list have 1 as their first digit are : ", x, "and in total there are:",len(x), "intergers that start with 1")
k = int(input("Please enter a search integer: "))
c = n_count(myArray,k)
print("11. The number of times that ", k, " is in the list =  ", c)









