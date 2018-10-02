import random
array = []
# empty list

n = 20
a = 0
b = 10
x = random.randint(a, b )
j = 0
size = 25
while (j < size):
    x = random.randint(a, b )
    # Return a random integer N such that a <= x <= b.
    array.append(x)
    j = j + 1
print("Step 0")
print("Populate an array(list) of size 25 with integers in the range 0  --- 10 inclusive")
print("array == ",array)


print("____________________________________________________________________________________")
print("Step 1")
print("Display the average of all the integers in the array")
sum = 0
for k in array:
    sum = sum + k
average_array = sum / len(array )
print(" The average of all the integers in the array is: ",average_array)


print("____________________________________________________________________________________")
print("Step 2")
print("Display the number of even integers  (how many)")
odd_number = 0
even_number = 0
for n in array:
    if n%2 != 0:
        odd_number = odd_number +1
    else:
        even_number = even_number +1

print( "The number of even integers is: ", even_number)

print("____________________________________________________________________________________")
print("Step 3")
print("Display the number of odd integers  (how many)")
print( "The number of odd integers is: ", odd_number)

print("____________________________________________________________________________________")
print("Step 4")
print("Display the median")
array.sort()
print("Sorted array: ", array )
print("The median is: ", array[12])
median_integer = array[12]

print("____________________________________________________________________________________")
print("Step 5")
print("Display the integers > median ")
#print("Integers > median are: ", array[13:])
high_integers=[]
for i in array [13:]:
    if i != median_integer :
        high_integers.append(i)
print("Integers > median are: ", set(high_integers))
print("____________________________________________________________________________________")
print("Step 6")
print("Display the integers < median ")

#print("Integers < median are: ", array[:12])
low_integers=[]
for i in array [:12]:
    if i != median_integer :
        low_integers.append(i)
print("Integers < median are: ", set(low_integers))

print("____________________________________________________________________________________")
print("Step 7")
print("Ask the user for an integer and print the number of times the integer is in the array ")
s = int(input("Please enter an integer between 0 and 10: "))

print("The integer ", s, " is ", array.count(s), " time(s) in the array. ")

print("____________________________________________________________________________________")
print("Step 8")
print("Display the maximum integer ")
print("The maximum integer in the array is : ", max(array))

print("____________________________________________________________________________________")
print("Step 9")
print("Display the minimum integer")
print("The minimum integer in the array is : ", min(array))




