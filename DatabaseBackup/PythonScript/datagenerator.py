# written by Lev C. Guzman Aparicio 300038033 lguzm038@uottawa.ca 2020
import csv
import random

########################################################################
####################### Generator for the users schema #################
########################################################################

# Generator for the users_info, guest_info, host_info

# pool of data used for users schema
header = ["account_id", "first_name", "middle_name", "last_name", "email", "phone_number",
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
                        "Arango", "Emiliano", "Madero", "Lenin", "Evgueni", "Yuri"]

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
                "h1n1", "h5n1", "tlatoani", "balam", "elote", "chachalaca",
                "postgres","quarantineboi", "quarantinegal", "alucard", "belmont", "quetzal"]


def generate_id_pool(seed_number):
    random.seed(seed_number)

    pool = []

    for i in range(100 * 10):
        random_id = random.randint(1, 500000)

        pool.append(random_id)

    return pool


pool_of_host_ids = generate_id_pool(120928487468718212)

pool_of_guest_ids = generate_id_pool(1293791461647381)

pool_of_account_ids = generate_id_pool(8736317677281)

# after generation of data, set seed to 1
random.seed(1)

with open('users_info.csv', 'w', ) as file:
    # opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)

    # generates 100 entries
    for i in range(100):
        # generate pseudorandom data

        account_id = random.sample(pool_of_account_ids, 1)
        account_id = account_id[0]
        first_name = random.choice(pool_of_names)
        middle_name = random.choice(pool_of_middle_names)
        last_name = random.choice(pool_of_last_names)
        email = random.choice(pool_of_emails) + ''.join(random.sample('0123456789', 3)) + "@service.com"
        phone_number = ''.join(random.sample('0123456789', 10))  # random phone number
        city = random.choice(pool_of_cities)
        country = random.choice(pool_of_countries)
        province_or_state = random.choice(pool_of_states)
        house_number = random.randint(1, 99)
        street_name = random.choice(pool_of_streets)

        data = [account_id, first_name, middle_name, last_name, email, phone_number, city,
                province_or_state, house_number, street_name]

        # writes it in the file
        writer.writerow(data)

# guest_id.csv generator

header = ["guest_id"]

with open('guest_id.csv', 'w', ) as file:
    # opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)

    # generates 100 entries
    for i in range(100):
        # generate pseudorandom data

        guest_id = random.sample(pool_of_guest_ids, 1)
        guest_id = guest_id[0]

        data = [guest_id]

        # writes it in the file
        writer.writerow(data)

# host_id generator
header = ["host_id"]

with open('host_id.csv', 'w', ) as file:
    # opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)

    # generates 100 entries
    for i in range(100):
        # generate pseudorandom data

        host_id = random.sample(pool_of_host_ids, 1)
        host_id = host_id[0]

        data = [host_id]

        # writes it in the file
        writer.writerow(data)

####################################################################
############### Generator for transactions schema ##################
####################################################################

# update the header following the schema
header = ["transaction_id", "type_of_payment", "payment_status", "host_collector_id",
          "amount"]

# generate transaction ids and reset seed to 1
pool_of_transaction_ids = generate_id_pool(192013008419033)

random.seed(1)

# generator for transactions info
with open('transactions_info.csv', 'w', ) as file:
    # opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)

    # generates 200 entries
    for i in range(200):
        # generate pseudorandom data

        transaction_id = random.sample(pool_of_transaction_ids, 1)
        transaction_id = transaction_id[0]
        type_of_payment = random.choice(["Cash", "Check", "Credit"])
        payment_status = random.choice(["Accepted", "Not Accepted"])
        host_collector_id = random.sample(pool_of_host_ids, 1)
        host_collector_id = host_collector_id[0]
        amount = random.randint(1, 30000)

        data = [transaction_id, type_of_payment, payment_status, host_collector_id, amount]

        # writes it in the file
        writer.writerow(data)

# generator for pricing table

# generate pool of property id
pool_of_properties_ids = generate_id_pool(1272121241576)
pool_of_pricing_ids = generate_id_pool(20120931731682)
pool_of_types = ["condo", "villa", "apartment", "basement", "mansion", "house", "room"]
rule_keywords = ["no pets", "no smoking", "only men", "only women"
    , "pets allowed", "no parties", "only cats", "no loud noises"]
amenities_keyword = ["pool", "induction stove", "garden", "safe lock", "library",
                     "private restroom", "large dining room"]

# reset the seed to 1 after using the generator
random.seed(1)

header = ["pricing_id", "allowed_number_of_guests", "valid_for_type", "rules", "amenities"]

with open('pricing.csv', 'w', ) as file:
    # opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)

    # generates 200 entries
    for i in range(200):
        # generate pseudorandom data
        pricing_id = random.sample(pool_of_pricing_ids, 1)
        pricing_id = pricing_id[0]
        allowed_number_of_guests = random.randint(0, 10)
        valid_for_type = random.choice(pool_of_types)
        rules = random.choice(rule_keywords)
        amenities = random.choice(amenities_keyword)

        data = [pricing_id, allowed_number_of_guests, valid_for_type, rules, amenities]

        # writes it in the file
        writer.writerow(data)

####################################################################################
##################### Generator for the Properties Schema ##########################
####################################################################################

# data used

# update header
header = ["property_id", "type", "number_of_rooms", "owner_id", "available_date", "pricing_id",
          "location"]


def generate_days(seed_number):
    random.seed(seed_number)
    pool = []

    for i in range(100 * 10):
        year = random.randint(1940, 2080)

        month = random.randint(1, 12)
        day = random.randint(1, 31)

        if month < 10:
            month = str(0) + str(month)

        if (day < 10):
            day = str(0) + str(day)

        pool.append(str(year) + "-" + str(month) + "-" + str(day))
    return pool


# reset seed
pool_of_dates = generate_days(111111112020)
random.seed(1)

with open('properties_info.csv', 'w', ) as file:
    # opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)

    # generates 200 entries
    for i in range(200):
        # generate pseudorandom data
        property_id = random.sample(pool_of_properties_ids, 1)
        property_id = property_id[0]
        tYpe = random.choice(pool_of_types)
        number_of_rooms = random.randint(1, 10)
        owner_id = random.choice(pool_of_host_ids)

        # the date format is YYYY-MM-DD.
        available_date = random.choice(pool_of_dates)

        pricing_id = random.sample(pool_of_pricing_ids, 1)
        pricing_id = pricing_id[0]
        location = random.choice(pool_of_states) + "," + random.choice(pool_of_countries)

        data = [property_id, tYpe, number_of_rooms, owner_id, available_date, pricing_id, location]

        # writes it in the file
        writer.writerow(data)


# method to generate two arrays of data

def generate_diff_days(seed):
    random.seed(seed)

    greaterPool = []
    lowerPool = []

    for i in range(100 * 10):
        year = random.randint(1940, 2080)
        year2 = random.randint(1930, 2090)

        month = random.randint(1, 12)
        day = random.randint(1, 31)

        if month < 10:
            month = str(0) + str(month)

        if day < 10:
            day = str(0) + str(day)

        if year > year2:
            greaterPool.append(str(year) + "-" + str(month) + "-" + str(day))
            lowerPool.append(str(year2) + "-" + str(month) + "-" + str(day))
        elif year2 > year:
            greaterPool.append(str(year2) + "-" + str(month) + "-" + str(day))
            lowerPool.append(str(year) + "-" + str(month) + "-" + str(day))
        else:

            greaterPool.append(str(year) + "-" + str(month) + "-" + str(day))
            lowerPool.append(str(year2) + "-" + str(month) + "-" + str(day))

    return greaterPool, lowerPool


# agreement_id

pool_of_agreement_ids = generate_id_pool(7647098363728942934)

pool_of_properties_ids = generate_id_pool(1272121241576)  # restore after use

pool_of_host_ids = generate_id_pool(120928487468718212)  # restore after use

pool_of_transaction_ids = generate_id_pool(192013008419033)  # restore after use

# 0 is for greater days, 1 is for lower days

pool_of_booking_days = generate_diff_days(56438719289134719)

random.seed(1)

header = ["agreement_id", "property_id", "start_date", "end_date", "host_grantor_id", "payment_id"
    , "pricing_id"]

with open('rental_agreement.csv', 'w', ) as file:
    # opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)

    # generates 100 entries
    for i in range(100):
        # generate pseudorandom data
        agreement_id = random.sample(pool_of_agreement_ids, 1)
        agreement_id = agreement_id[0]

        property_id = random.sample(pool_of_properties_ids, 1)
        property_id = property_id[0]

        start_date = random.sample(pool_of_booking_days[1], 1)
        start_date = start_date[0]

        end_date = random.sample(pool_of_booking_days[0], 1)
        end_date = end_date[0]

        host_grantor_id = random.sample(pool_of_host_ids, 1)
        host_grantor_id = host_grantor_id[0]

        payment_id = random.sample(pool_of_transaction_ids, 1)
        payment_id = payment_id[0]

        data = [agreement_id, property_id, start_date, end_date, host_grantor_id, payment_id, pricing_id]

        # writes it in the file
        writer.writerow(data)

#####################################################################################################
#################################### Generator for the Management Schema ############################
#####################################################################################################

header = ["branch_id", "branch_name", "country", "num_employees", "manager_id"]

# generate id pool and reset seed to 1
pool_of_branch_ids = generate_id_pool(62884093871982)
pool_of_employee_ids = generate_id_pool(89228748493221)
random.seed(1)

with open('branch_info.csv', 'w', ) as file:
    # opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)

    # generates 100 entries
    for i in range(100):
        # generate pseudorandom data

        branch_id = random.sample(pool_of_branch_ids, 1)
        branch_id = branch_id[0]

        branch_name = random.sample(pool_of_countries, 1)
        branch_name = branch_name[0]
        country = branch_name

        num_employees = random.randint(1,1000)

        manager_id = random.sample(pool_of_employee_ids, 1)
        manager_id = manager_id[0]

        data = [branch_id, branch_name + " branch", country, num_employees, manager_id]

        # writes it in the file
        writer.writerow(data)

# employee_info data generator

header = ["employee_id", "first_name", "last_name", "city", "country", "works_for_branch_id"
          , "email", "phone_number", "salary", "position", "street_name", "street_number"]

pool_of_employee_ids = generate_id_pool(89228748493221)  # regenerate
pool_of_branch_ids = generate_id_pool(62884093871982)  # regenerate
random.seed(1)

pool_of_countries = ["Mexico", "United States", "Canada",
                     "Japan", "Colombia", "Peru", "Brazil",
                     "USSR", "Russia", "Ukraine", "Belorussia",
                     "Portugal", "Spain", "Tenochtitlan", "China", "Indonesia", "Bolivia"] #regenerate

pool_of_employee_names = ["Salvador", "Monica", "Monique", "Theodore", "Ronald", "Sullivan",
                          "Ted", "Bernie", "Joe", "Steve", "Joseph", "Jonathan", "Dio", "Robert",
                          "Jolyne", "Josuke"]

pool_of_employee_last_names = ["Speedwagon", "Brando", "Joestar", "Kujo", "Cujoh", "Costello",
                               "Dali", "Hernandez", "Espinoza", "Higashikata", "Perez", "Nijimura"
                               "Conrado", "Torres"]

pool_of_employee_emails = ["vampirehunter", "pianomaster", "professional", "employee", "mathpro",
                           "diavolo", "bunny", "babyshark", "daddyshark" , "mommyshark", "eloteasado"
                           , "cactus", "panteon"]

pool_of_positions = ["cleaner", "counter", "broker", "estate agent", "manager", "IT support"]

pool_of_employee_street_name = ["Cuyo", "Juarez", "Wuhan", "Warudo", "Papaya", "Melon", "Time"
                                 "Grove", "Fish", "Megalodon", "Pollo", "Doll", "Bucciarati", "Mista"
                                 "Trish", "Fugo"]

with open('employee_info.csv', 'w', ) as file:
    # opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)

    # generates 100 entries
    for i in range(100):
        # generate pseudorandom data

        employee_id = random.sample(pool_of_employee_ids, 1)
        employee_id = employee_id[0]

        first_name = random.choice(pool_of_employee_names)
        last_name = random.choice(pool_of_employee_last_names)

        city = random.choice(pool_of_cities)
        country = random.sample(pool_of_countries,1)
        country = country[0]

        works_for_branch_id = random.sample(pool_of_branch_ids,1)
        works_for_branch_id = works_for_branch_id[0]

        email = random.choice(pool_of_employee_emails) + ''.join(random.sample('0123456789', 4)) + "@employee.com"

        phone_number = ''.join(random.sample('0123456789', 10))

        position = random.choice(pool_of_positions)

        if position == 'manager':
            salary = random.randint(5000, 10000)
        else:
            salary = random.randint(1000, 3000)

        street_name = random.choice(pool_of_employee_street_name) + " street"
        street_number = random.randint(0, 999)

        data = [employee_id, first_name, last_name, city, country, works_for_branch_id
                , email, phone_number, salary, position, street_name, street_number]

        # writes it in the file
        writer.writerow(data)

# review_info data generator
# for reviewer_id = guest_id
header = ["review_id", "reviewed_property_id", "reviewer_id", "number_of_stars", "guest_comments",
          "cleanliness_of_property"]

pool_of_review_ids = generate_id_pool(456849328737191)
pool_of_properties_ids = generate_id_pool(1272121241576)
pool_of_guest_ids = generate_id_pool(1293791461647381)

pool_of_positive_comments = ["city is close", "downtown vibes", "good price", "good experience",
                    "very large", "very comfy", "feels like home", "absolute tranquility", "everything works"]

pool_of_negative_comments = ["terrible", "very small", "bathroom does not work", "with very visible faults",
                             "no restaurants nearby", "has rats", "has cockroaches"]

pool_of_neuter_comments = [" ", "no comments", "okay-ish", "good for price"]

random.seed(1)

with open('review_info.csv', 'w', ) as file:
    # opens the file and writes the header
    writer = csv.writer(file)
    writer.writerow(header)

    # generates 100 entries
    for i in range(100):
        # generate pseudorandom data

        review_id = random.sample(pool_of_review_ids,1)
        review_id = review_id[0]

        reviewed_property_id = random.choice(pool_of_properties_ids)

        reviewer_id = random.choice(pool_of_guest_ids)

        number_of_stars = random.randint(1, 5)
        cleanliness_of_property = random.randint(1,5)

        if number_of_stars < 6 and number_of_stars > 3:
            guest_comments = random.choice(pool_of_positive_comments)
        elif number_of_stars <3 and number_of_stars > 0:
            guest_comments = random.choice(pool_of_negative_comments)
        else:
            guest_comments = random.choice(pool_of_neuter_comments)

        data = [review_id , reviewed_property_id, reviewer_id, number_of_stars, guest_comments,
                cleanliness_of_property]

        # writes it in the file
        writer.writerow(data)
