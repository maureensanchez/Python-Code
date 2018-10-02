C1 = 29
C2 = 6
C3 = -5

x = int(input(" Please enter integer ..."))
y = int(input(" Please enter another integer ..."))
z = int(input(" Please enter the third integer ..."))

print("The numbers entered are ", x," , ", y, " and ", z)

# this is a comment
#the following if...else structure is used to illustrate the syntax
# note the identation
if (x > 0) :
    h1 = C1*x
    h2 = C2*x
else:
    h1 = C2*y
    h2 = C3*y
#print("values h1 = ", h1, " and ", " h2 ", h2)

sum = x + y + z
print("The sum of the intergers is  = ", sum,)
p = x*y*z
print("The product of the intergers is  = ", p )
sum_raised = sum**x
print("The sum raised to the power of the first  integer is:  ", sum_raised)
sum_divided = sum/y
print("The sum divided by the second  integer is:  ", sum_divided)
sum_divided_2 = sum//z
print("The sum divided by the third  integer is:  ", sum_divided_2)
remainder = sum%x
print("The remainder of the division of sum by the first integer is:  ", remainder)
m = max(x,y,z)  # MAX function similar function for min
print("The maximun is:  ", m)
mini = min(x,y,z)  # MAX function similar function for min
print("The minimum is:  ", mini)
average = sum/3  # MAX function similar function for min
print("The average is:  ", average)
