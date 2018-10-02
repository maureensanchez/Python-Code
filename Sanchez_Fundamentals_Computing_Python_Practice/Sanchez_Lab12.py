import random
from statistics import median

def fill(ax,nx, x,y):       # fill the list a with n random integers in the range x --- y inclusive BUT NO duplicates permitted THIS code NEEDS to be fixed
    j = 0
    while (j < nx):  # populate the array using the while loop
        a = random.randint(x, y)  # Return a random integer .
        if a not in ax:
          ax.append(a)
          j = j + 1
    return ax
def display(ax):
    print("2. Display the list as follows: ", ax)  # DONE


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



def div3(ax):
    count_three = 0
    for i in ax:
        if i % 3 == 0:
            count_three = count_three + 1
    return count_three
    # v = -5
    # return v

def multi5(ax):
    count_five = 0
    for i in ax:
        if i % 5 == 0:
            count_five = count_five + 1
    return count_five
    # m = 11
    # return m

def avg_of_list(ax):
    # return the average of the integers in the list
    #must call the sum() function here and divide by the size of the array
    size_of_array = sum(ax)
    average_list = size_of_array/len(ax)
    return average_list


def maximum(ax):
    # return the largest value in the list
    mx = ax[0]  # place holder only
    return mx

def minimum(ax):
    # return the smallest value in the list
    mn = ax[-1]
    return mn

def median_number(ax):
    med = median(ax)
    return med

def digit1(ax):
    list_ones = [11,21,31]
    count_end_one = 0
    for i in ax:
        if i in list_ones:
            count_end_one = count_end_one + 1
    return count_end_one

# ==========================================
# NOW we call the functions
#Suggested template i.e all calculations should be in the functions; simply call the functions
array = []
n = 21  # array size
x = 10
y = 40
array = fill(array,n, x, y)
display(array)
mx = max_integer(array)
mn = min_integer(array)
d = div3(array)
m = multi5(array)
med = median_number(array)
n1 = digit1(array)
array = sort_list_asc(array)
ave = avg_of_list(array)
print("3. The sorted list in descending order is ", array)
print( "4. The maximum integer in the list  is  : ", mx )
print( "5. The minimum integer in the list  is :", mn)
print( "6. The number of integers that are evenly divisible by 3 (no remainder)is : ", d)
print( "7. The number of integers in the list that are multiples of 5 (10, 15, 20,25, etc ) is : ", m)
print( "8. The median of the list is : ", med)
print( "9. the number of integers that end with a 1 is : ", n1)
print("10. The average of the integers is ", round(ave), ".( Please note the number is rounded.)")
