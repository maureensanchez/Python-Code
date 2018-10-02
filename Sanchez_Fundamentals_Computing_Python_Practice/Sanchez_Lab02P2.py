A = 30  #CONSTANT fee for <= 300 minutes
m = int(input("Enter the number of minutes: "))
c = 0  # initialize cost variable
if (m > 300):        # minutes > 300
    # calculations here to compute the solution
    # use the correct answer provided
    c = 30 + (m -300) * .45
    print(" the cost for ", m, " minutes  is $:  ", c )
else:    # here m is <= 300           # s <= 0
    print(" the cost for ", m, ' minutes is $: ', A )
