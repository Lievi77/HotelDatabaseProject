#written by Lev C. Guzman Aparicio 300038033 lguzm038@uottawa.ca 2020
import csv
import psycopg2
import random
import string

#generates 100 instances of data for each of our tables.

#seed that will be used
random.seed(1)

####################### Generator for the users schema #################

# Generator for the users_info, guest_info, host_info

header = ["host_id", "first_name", "middle_name", "last_name", "email", "phone_number",
            "city", "country", "province_or_state", "house_number", "street_name"]

pool_of_states = ["California",
                    "Mexico", "Ciudad de Mexico",
                    "Ontario", "Nunavut", "Nova Scotia",
                    "Tlaxcala", "Oaxaca",
                    "New Jersey", "Quebec", "Alberta",
                    "Texas", "New Mexico", "Sonora", "Chihuahua",
                    "Tamaulipas", "Baja California"]

pool_of_names = ["Savy", "Camron", "Lev ", "Chris", "Cesar", "Andrew", "David", "Sam"
                , "Parth", "Anne", "Melissa", "Monica", "Rebeca", "Ehecatl",
                "Jason", "Sandy", "Eli"]

pool_of_middle_names = [" ", "Chavez", "Emilio",
                        "Gutierrez", "Samantha", "Roberto",
                        "Tonatiuh", "Colibri", "Santana", "Villa", "Doroteo",
                        "Arango","Emiliano","Madero","Lenin","Evgueni","Yuri"]

pool_of_last_names = ["Guzman", "Aparicio",
                     "Mika", "Eufracio", "Branco",
                     "Zarepour", "Choolhon", "Bundhoo",
                     "Sekhon", "Pochapsky",
                     "D'souza", "Wedia", "Wu", "Li", "Zepali",
                     "Bengali", "Hernandez"]

pool_of_cities = ["Texcoco", "Ottawa",
                    "Herst", "Tlaxcala",
                    "Oaxaca", "Toronto", "Halifax",
                    "Tizatlan", "Missasauga", "White Plains",
                    "New York", "Nezahualcoyotl", "Mexico City",
                    "Hamilton", "Cafe Pisado", "Mazunte", "Mazatlan"]

pool_of_countries = ["Mexico", "United States", "Canada",
                    "Japan", "Colombia", "Peru", "Brazil",
                    "USSR", "Russia", "Ukraine", "Belorussia",
                    "Portugal", "Spain", "Tenochtitlan", "China", "Indonesia", "Bolivia"]

pool_of_streets = ["34 St", "67 St",
                    "Grand Avenue", "Laurier Avenue East",
                    "Laurier Avenue West", "Main St", "Calzada de los Muertos",
                    "Prolongacion Popocatepetl",
                    "Sauna St", "Verdugo St", "Connect St",
                    "Calle Conejo", "Avenida Tecolote",
                    "Calle Escuadron 301", "Elign St", "Bank St", "Exodus Avenue"]
                    
pool_of_emails = ["combo", "user", "king", "queen", "sars", "mers"
                "h1n1", "h5n1", "tlatoani", "balam", "elote", "chachalaca", "postgres",
                "quarantineboi" , "quarantinegal" , "alucard", "belmont" , "quetzal"]

with open('users_info.csv', 'w', ) as file:
    #opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)
    
    #generates 100 entries
    for i in range(100):

        #generate pseudorandom data
        
        host_id = random.randint(1, 20000)
        first_name = random.choice(pool_of_names)
        middle_name = random.choice(pool_of_middle_names)
        last_name = random.choice(pool_of_last_names)
        email = random.choice(pool_of_emails) + ''.join(random.sample('0123456789', 3)) +"@service.com"
        phone_number = ''.join(random.sample('0123456789', 10)) #random phone number
        city = random.choice(pool_of_cities)
        country = random.choice(pool_of_countries)
        province_or_state =  random.choice(pool_of_states)
        house_number = random.randint(1, 99)
        street_name = random.choice(pool_of_streets)

        data = [host_id, first_name, middle_name, last_name, email, phone_number, city,
            province_or_state, house_number, street_name  ] 

        #writes it in the file
        writer.writerow(data)
