

height = float(input("Enter your height in meters: "))


weight =float(input("Enter your weight in kg's: "))


def calculate_bmi():

    BMI = weight / height**2

    print("Your BMI is" + " " + str(BMI))

calculate_bmi()




