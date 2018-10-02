# CSC120
# Using the list defined as a  below, write a Python program that will
a = [ "Euclid", "Archimedes", "Newton","Descartes", "Fermat", "Turing", "Euler", "Einstein", "Boole", "Fibonacci", "Nash"]
print ('List : ', a)
# Define Variables
j = 0
i = 0
q = 0
b=0
c=0
d = 0
maxlen =0
list_together = ''
# 1.	Display the longest name (done #12 below )
for y in a:
    list_together = list_together + a[d]
    d = d+1
for k in a:
    if len(a[j])> maxlen:
        maxlen = len(a[j])
        t = a[j]
    j = j+1
print("1. The longest name is :  ", t )
#2 .	Display the shortest name
minlen = 999999

for k in a:
    if len(a[i]) < minlen:
        minlen = len(a[i])
        tt = a[i]
    i = i+1
print("2. The shortest name is :  ", tt)
#3 .	Display the number of names in the list NOTE: your answer should be 11 but do NOT use the constant 11 in your output;  code the size of the list
print("3. The size of the list is :  ", len(a))
#4 .	Display a string that consists of the first letter from each of 11 names in the list a
#See 9 in the output and consider using the  + operator  Must use a loop


names = ''
for y in a:
    names = names + a[q][0]
    q = q+1
print("4. A string that consists of the first letter from each of 11 names is  :  ",names)
#5.	Display a string that consists of the last letter from each of 11 names in the list a
#See 10 in the output  Must use a loop

last_names = ''
for y in a:
    last_names = last_names + a[b][-1]
    b = b+1
print("5. A string that consists of the last letter from each of 11 names is  :  ",last_names)
#6.	Ask the user for a letter.  Display the number of times the letter appears in the list See the count function from the prior labs
question  = (str(input(" Please enter a letter: "))).lower()
lower_list = list_together.lower()
check_count = 0
for y in lower_list:
    check_count = check_count + lower_list[c].count(question)
    c = c+1


print("6. The number of times the letter", question, " appears in the list   :  ",check_count)
#7.	Sort list a and display the list  i.e. the first name in the list should be Archimedes; last name is Turing
print( "7. The sorted list looks like this: " , sorted(a))
#8.	Sort the list in reverse order and display the  list i.e. the first name should be Turing and the last Archimedes
print( "8. The reversed sorted list looks like this: " , sorted(a, reverse = True))
#9.	Display the number of vowels 	Vowels are { ‘A’, ‘a’, ‘E’, ‘e’, ‘I’, ‘I’,  ‘O’, ‘o’, ‘U’, ‘u’ }
counts = {i:0 for i in 'aeiouAEIOU'}

for char in list_together:
  if char in counts:
   counts[char] += 1

print( "9. The the number of vowels are : " ,counts,)


