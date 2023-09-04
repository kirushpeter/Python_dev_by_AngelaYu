
def get_BMI (height, weight):

    #height = float(input("Enter your height: "))

    #weight = float(input("Enter your weight: "))

    BMI = weight / height ** 2


    print(BMI)

    


    if BMI <= 15:
      
      print("You are critically underweight")

    elif BMI <= 25:

      print("You are not obesse")

    elif BMI <= 30:

      print("You are obesse")

    else:
      print("You are critically obesse")


    

    #return(BMI)

     
#get_BMI(1.25, 78)


get_BMI(float(input("Enter your height: ")),float(input("Enter your weight: ")))



    

