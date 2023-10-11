import listas
import random

while True:
    
    print("Welcome to the data Generator for Tests - To stop the program, write 'stop' ")
    print("--------------------------------------------------------------------------")

    input1 = input("""Chose one or more options below to generate randonly:
        [1] - Name
        [2] - E-mail
        [3] - Telephon
        [4] - City
        [5] - State
        You can chose more them one option : """)

    if 'stop' in input1:
        break  

    print("--------------------------------------------------------------------------")

    input2 = input('Would you like to save the data in a txt file?(y/n)')
    
    
    def process_data(data_string):
        output =''
        
        if '1' in data_string:
            name = random.choice(listas.names)
            output = output + name + '\n' 
        if '2' in data_string:
            email = random.choice(listas.email)
            output = output + email + '\n' 
        if '3' in data_string:
            phone_number = random.choice(listas.phone_numbers)
            output = output + phone_number + '\n' 
        if '4' in data_string:
            city = random.choice(listas.cities)
            output = output + city + '\n' 
        if '5' in data_string:
            state = random.choice(listas.states)
            output = output + state + '\n'
        
        return output 

    data_processed = process_data(input1)
    print(data_processed)

    if input2 == 'y':
        with open('data.txt','a') as file:
            file.write(data_processed)



              