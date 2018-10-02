import math
rate1 = 5  # $5 rate
rate2 = 4  # $4 rate
rate3 = 2  # $2 rate

# initialize
m = int(input(" Please enter number of minutes parked..."))

#table 1
if (0 < m and m <= 60 ):
    #hrs = int(m/60)
    fee = rate1
    print("Parking fee for ", m, " minutes is $", fee)

# now for table 2
elif m > 60 and m <= 300:     # table 2
    # calculations needed
    hrs = math.ceil(m/60)
    fee = hrs * rate2
    print("Parking fee for ", m, " minutes is $", fee)

# table 3
elif  m > 300:
    # calculations needed
    hrs = math.ceil(m/60)
    fee = hrs * rate3
    print("Parking fee for ", m, " minutes is $", fee)

else:
    print("Error  negative minutes : ", m )
