Name = input(print("Write your name to start your BMI value calculation: ")) 
# stores the users input

print(f"Welcome {Name} ")  # print the user input


Weight = float(input(print("Enter your weight value in KG's: ")))

Height = float(input(print("Enter your height in Meters: ")))

BMI = Weight / Height**2

if BMI < 18.5:

    print("You are undereight")

elif BMI < 25:

    print("You are in healthy weight range")

elif BMI < 30:

    print("You are in the overweight range")

else:
    print("You are obese")





