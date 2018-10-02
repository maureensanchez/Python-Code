import random
import math

N = 30
M = 50
#dictionary
dictionary_messages  = { 2: "Greetings and salutations!", 3: "What is up?", 4: "You are slow!", 5: "All your trinkets belong to us.",
    6: "Someone on our team thinks someone on your team are in the same class.", 7: "You are the weakest link.",
    8: "Encryption is fun", 9: "Spring is my favorite season", 10: "Enjoy your morning beverage",
    11: "I am an early riser", 12: "I am not an early riser", 13: "Pick up your toys" }
print ("dictionary",dictionary_messages )
print("keys",dictionary_messages .keys())
print("values", dictionary_messages .values())
print("keys one",dictionary_messages [3])

# # select a key and display value
# i= 8
# print(" dictionary value for key ", i, " is ", d[8])

# select two primes between N and M call them p q you select these primes
# determine an encryption key e and a decryption key d based on the algorithm on the next page
# example ONLY
two_numbers = []
one =1
count = 3#1.	Choose primes p and q to be relatively small, say in the range 30--50. In practice, p and q might contain hundreds of digits, but small numbers are easier.

def fill(ax,nx, x,y):       # fill the list a with n random integers in the range x --- y inclusive BUT NO duplicates permitted THIS code NEEDS to be fixed
    j = 0
    while (j < nx):  # populate the array using the while loop
        a = random.randint(x, y)  # Return a random integer .
        if a not in ax:
          ax.append(a)
          j = j + 1
    return ax
array = []
n = 2  # array size
x = 30
y = 50
array = fill(array,n, x, y)
print("First number randomly selected, p =",array[0])
print("Second number randomly selected, q = ",array[1])
p = array[0]
q = array[1]
e = 5
d = 29
n = p*q

two_numbers = []
one =1
count = 3#1.	Choose primes p and q to be relatively small, say in the range 30--50. In practice, p and q might contain hundreds of digits, but small numbers are easier.
while one == 1:
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                continue
            if count % x != 0:
                two_numbers.append(x)

        count += 1

print( two_numbers)

print("the two primes are ", p, '..', q)
print(" n == ", n)
totient = (p-1)*(q-1)
print("Maureen phi",totient)

a = 60
b= 48

def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)



# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (hcfnaive(60,48))
if d * e == 1 % totient:
    print(" The decrypting key is:", d)


print("the encryption key is ", e, ' decryption key is ', d)
#print (" the value of e*d%n == ", e*d%n )       # e*d % n should be 1
# use the message m values below
m = int(input("please enter a message [2...13] "))
print(m)
c = m ^ e % n  # needs to be fixed this is the cypher message

print (c, " is computed using the calculation m^e mod n  ")  # ^ == exponentiation
print("the encrypted message is ", c )
print("the decrypted message is ", m )

print (m, " is computed using the calculation c^d mod n")
# for key in d:
for k, v in dictionary_messages.items():
    if k == m :
        print("the text associated with : {0}, is : {1}".format(k, v))
        #print("the text associated with ", m, " is ", d[key] )

array = []
n = 2  # array size
x = 30
y = 50
array = fill(array,n, x, y)
print(array)
