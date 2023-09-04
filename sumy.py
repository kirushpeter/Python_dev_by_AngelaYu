
#Identation of the print function produces different results 

#printing sum of numbers in the range of 0 to 100.


print("Start of the first calculation")

sum = 0

items = range(0, 101)

for nums in items:

    sum += nums

print(sum)

print("End of second calculation")

print(" \n")

print("Start of second calculation")

sum = 0

for nums in range(0, 101):

    sum += nums

print(sum)

print("End of second calculation")