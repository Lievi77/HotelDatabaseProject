#written by Lev C. Guzman Aparicio 300038033 lguzm038@uottawa.ca 2020
import csv
import psycopg2
import random
import string

########################################################################
####################### Generator for the users schema #################
########################################################################

# Generator for the users_info, guest_info, host_info

#pool of data used for users schema 
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
                "Jason", "Sandy", "Omer"]

pool_of_middle_names = [" ", "Chavez", "Emilio",
                        "Gutierrez", "Samantha", "Roberto",
                        "Tonatiuh", "Colibri", "Santana", "Villa", "Doroteo",
                        "Arango","Emiliano","Madero","Lenin","Evgueni","Yuri"]

pool_of_last_names = ["Guzman", "Aparicio",
                     "Mika", "Eufracio", "Branco",
                     "Zarepour", "Choolhon", "Bundhoo",
                     "Sekhon", "Pochapsky",
                     "D'souza", "Wedia", "Wu", "Li", "Abubaker",
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
                "quarantineboi", "quarantinegal", "alucard", "belmont", "quetzal"]

def generateIDPool(seed_number):
    random.seed(seed_number)

    pool = []

    for i in range(100):

        random_id = random.randint(1, 20000)

        pool.append(random_id)
    
    return pool

pool_of_host_ids = generateIDPool(2)

pool_of_guest_ids = generateIDPool(3)

pool_of_account_ids = generateIDPool(4)

#after generation of data, set seed to 1
random.seed(1)

with open('users_info.csv', 'w', ) as file:
    #opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)
    
    #generates 100 entries
    for i in range(100):

        #generate pseudorandom data
        
        host_id = random.choice(pool_of_account_ids)
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


#guest_id.csv generator

header = ["guest_id"]

with open('guest_id.csv', 'w', ) as file:
    #opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)
    
    #generates 100 entries
    for i in range(100):

        #generate pseudorandom data
        
        data = [ random.choice(pool_of_guest_ids) ] 

        #writes it in the file
        writer.writerow(data)

#host_id generator
header = ["host_id"]

with open('host_id.csv', 'w', ) as file:
    #opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)
    
    #generates 100 entries
    for i in range(100):

        #generate pseudorandom data
        
        data = [ random.choice(pool_of_host_ids) ] 

        #writes it in the file
        writer.writerow(data)


####################################################################
############### Generator for transactions schema ##################
####################################################################

#update the header following the schema
header = ["transaction_id", "type_of_payment", "payment_status", "host_collector_id",
        "amount"]

#generate transaction ids and reset seed
pool_of_transaction_ids = generateIDPool(5)
random.seed(1)

#generator for transactions info
with open('transactions_info.csv', 'w', ) as file:
    #opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)
    
    #generates 200 entries
    for i in range(200):

        #generate pseudorandom data
        
        transaction_id = random.choice(pool_of_transaction_ids)
        type_of_payment = random.choice(["cash", "check", "credit"])
        payment_status = random.choice(["Accepted", "Not Accepted"] )
        host_collector_id = random.choice(pool_of_host_ids)
        amount = random.randint(1,30000)

        data = [transaction_id, type_of_payment, payment_status, host_collector_id, amount ] 

        #writes it in the file
        writer.writerow(data)

#generator for pricing table

#generate pool of property id
pool_of_properties_ids = generateIDPool(6)
pool_of_types = ["condo", "villa", "apartment", "basement", "mansion", "house", "room"]
rule_keywords = ["no pets", "no smoking", "only men", "only women"
                , "pets allowed", "no parties", "only cats", "no loud noises"]
amenities_keyword = ["pool", "induction stove", "garden", "safe lock", "library",
                    "private restroom", "large dining room"]

#reset the seed to 1 after using the generator
random.seed(1)

header = ["property_priced_id", "allowed_number_of_guests", "valid_for_type", "rules", "amenities"]

with open('pricing.csv', 'w', ) as file:
    #opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)
    
    #generates 200 entries
    for i in range(200):

        #generate pseudorandom data
        property_priced_id = random.choice(pool_of_properties_ids)
        allowed_number_of_guests = random.randint(0, 10)
        valid_for_type = random.choice(pool_of_types)
        rules = random.choice(rule_keywords)
        amenities = random.choice(amenities_keyword)

        data = [property_priced_id, allowed_number_of_guests, valid_for_type, rules, amenities] 

        #writes it in the file
        writer.writerow(data)

####################################################################################
##################### Generator for the Properties Schema ##########################
####################################################################################

#data used

#update header
header = []

with open('properties_info.csv', 'w', ) as file:
    #opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)
    
    #generates 200 entries
    for i in range(200):

        #generate pseudorandom data
       
        

        data = [] 

        #writes it in the file
        writer.writerow(data)