states = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut','Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 
        'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont','Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 
        'Mississippi','Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan','Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 
        'Minnesota','Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado','North Dakota', 'South Dakota', 'Montana', 'Washington', 
        'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']


print(states)

'''
Objects - Consist of properties and behaviour | properties of the object are defined by the attributes and the behaviour is defined using methods.


Methods - defined inside a class

        - these methods are the reusable piece of code that can be invoked/called at any point in the program
        - There are basically three types of methods in python 

                     - Instance method - Used to set or get details about instances (objects) 

                                       - Have a default parameter self,



                     - Class method - purpose of the class method is to set or get the details(status) of the class

                                    - defined with the help of the classmethod decorator. @.


                     


                     - Static method -Static method cannot access the class data | They are self-sufficient and can work on their own.

                     

'''

# To add an item to the end of the list

states.append("New state")

print(states)

