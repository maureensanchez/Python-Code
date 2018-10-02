#CSC120Lab08Template

# Declare Variables
a = ["Euclid", "Archimedes", "Newton", "Descartes", "Fermat",
     "Turing", "Euler", "Einstein", "Boole", "Fibonacci",
     "Nash", "Wiles", "Cantor", "Gauss", "Plato"]  # Initial list n == 15
q = 0
j = 0
cnt = 1
total_lenght = 0
back_list_together= ''
names = ''
back = ''
back_names = []
all_first_last = []
d = 0
r = 0
total_char =0
#1.	Display a string that consists of the first letter and last letter from each of the names in the list a
# The output should look like “EdAsNn etc.  use the + operator or the append() function  from prior lab

for y in a:
    names = names + a[q][0] + a[q][-1]
    q = q+1
print("1. A string that consists of the first letter and last letter from each of the names in the list is: ",names)

#2.	Display  list a with all the names reversed that is display
#“dilcuE”, sedemihcrA” etc.

for y in a:
    back = y[::-1]

    all_first_last.append(back)
print ("2. A list a with all the names reversed is: ",all_first_last)

#3.	Display the total number of characters in the list a  Hint: Sum the lengths of each name
for y in a:
    back_list_together = back_list_together + a[d]
    d = d+1
print("3. The total number of characters in the list a is: ",len(back_list_together))
# 4.	In the prior lab we determined the number of vowels in the list.  For this lab, display the number of consonants
# (non-vowels) Use your result from 3.   to assist in the calculations
counts = {i:0 for i in 'BCDFGHJKLMNPQRSTVWXYZ'}
back_list_together = back_list_together.upper()
for char in back_list_together:
  if char in counts:
   counts[char] += 1
   total_char = total_char + len(char)
print("4. The total number of consonants are: ",total_char)
#5.	Display the number of each letter in the list NOTE ignore case ‘A’ and ‘a’  are to be considered the same.
print( "5. The total  number of each  consonants are : " ,counts,)
#6.	Display the average length of the strings in the list.   Remember to use the results from 3 and divide by n
n = len(a)
print("6. The average length of the strings in the list is: ", len(back_list_together) /n )


