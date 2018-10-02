keys_string = (input("Please enter a string : "))
length = len(keys_string)
values = list(keys_string)
keys = []
p= 0
while p < length:
    for i in values:
        keys.append(p)
        p = p +1

print(" Your string has ", length, "characters")

dictionary = dict(zip( keys, values))
print(dictionary)

string_of_digits =(input("Please enter a string of digits : "))
length_of_numbers = len(string_of_digits)
print("length_of_numbers", length_of_numbers)

numbers = []
t = 0
while t < length_of_numbers:
   for i in string_of_digits:
       numbers.append(i)
       t = t +1
print("this are the numbers:", numbers )

for j in string_of_digits:
    if j in dictionary.keys():
        print("test", j)

    else:

         print("Error in unput. please enter digits within the lenght of your string ")
         string_of_digits = (input("Please enter a string of digits : "))
