# CSC120
# Lab 06 Binomial distribution

import random
import  math
# Initialize array
myArray = []
a = 0
b = 1
size = 50
j = 0
n = 1000
# Populate array with size = 50 random integers in the range 0 - 1
#and repeat for n times
while (j < n):
    for k in range(size):
        randNum = random.randint(a,b)
        myArray.insert(k, randNum)
    j = j + 1

# Display array  size
print("size of my array is :", len(myArray))
# printmyArray  10 values per line 
k = 0
sub = []
while (k < len(myArray) ):
    sub = myArray[k: k+10]
    print("...",k, sub)
    k = k+10

ones = myArray.count(a)
zeros =myArray.count(b)
print(" number of 1 is: ", ones)
print(" number of 0 is: ", zeros)
sucess_of_1 = ones/len(myArray)
print("sucess of 1 : " , sucess_of_1)
# mean and standard deviation (sd) calculations here
#EXAMPLE ONLY

mean = 50000 * .5
sd = (50000 * .5 *(1 - .5))**.5
print("=====================")
print('mean of My Array:', mean, " sd (standard deviation: ", sd)
print (" mean +-sd:  ",mean - sd, "  " , mean + sd )
print ("the mean number of 1's is within mean +- sd ??? YES/NO ")     
# need to answer this 
# compare the number of 1s (variable zeros calculated above
# to see if it is within the range mean  sd.
print("Yes, the numbers of 1's is within the range.")
