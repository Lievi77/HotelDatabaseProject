# written by Lev C. Guzman Aparicio 300038033 lguzm038@uottawa.ca 2020
import psycopg2
<<<<<<< HEAD
import traceback
=======
>>>>>>> 3110543e902fce144c56ad94eecb5d1831b2b64b

################################################
# script that inserts data recorded in csv files
###############################################
<<<<<<< HEAD

# connection setup
conn = None

try:
    #Change variables in here to match your specifications
    conn = psycopg2.connect(host="localhost",database="travelapp", user="postgres", password="faiz123")
    print("Connection to database successfull, starting inserts!")
####################################################
######## Data insertor for USERS schema ###########
###################################################
    cur = conn.cursor()

    with open('guest_id.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'users.guest', sep=',')

    conn.commit()
    

    with open('host_id.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'users.host', sep=',')

    conn.commit()



    cur = conn.cursor()

    with open('users_info.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'users.user_info', sep=',')

    conn.commit()
    print("User schema data insertion complete...")
=======
# connection setup

conn = psycopg2.connect("host= web0.eecs.uottawa.ca dbname= lguzm038 user = lguzm038 password = Kyorzkyre77! port = 15432")

cur = conn.cursor()

cur.execute("TRUNCATE users.user_info CASCADE;")
cur.execute("TRUNCATE users.host CASCADE;")
cur.execute("TRUNCATE users.guest CASCADE;")
cur.execute("TRUNCATE transactions.payment_info CASCADE;")
cur.execute("TRUNCATE transactions.pricing CASCADE;")
cur.execute("TRUNCATE properties.properties_info CASCADE;")
cur.execute("TRUNCATE properties.rental_agreement CASCADE;")
cur.execute("TRUNCATE management.branch_info CASCADE;")
cur.execute("TRUNCATE management.employee_info CASCADE;")
cur.execute("TRUNCATE management.review_info CASCADE;")



####################################################
######## Data insertor for USERS schema ###########
###################################################
cur = conn.cursor()

with open('guest_id.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'users.guest', sep=',')

conn.commit()

with open('host_id.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'users.host', sep=',')

conn.commit()

cur = conn.cursor()

with open('users_info.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'users.user_info', sep=',')

conn.commit()
>>>>>>> 3110543e902fce144c56ad94eecb5d1831b2b64b

####################################################
######## Data insertor for TRANSACTIONS scheme ####
###################################################

<<<<<<< HEAD
    cur = conn.cursor()

    with open('transactions_info.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'transactions.payment_info', sep=',')

    conn.commit()

    cur = conn.cursor()

    with open('pricing.csv', 'r') as f:
     # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'transactions.pricing', sep=',')

    conn.commit()
    print("Transaction schema data insertion complete...")
=======
cur = conn.cursor()

with open('transactions_info.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'transactions.payment_info', sep=',')

conn.commit()

cur = conn.cursor()

with open('pricing.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'transactions.pricing', sep=',')

conn.commit()
>>>>>>> 3110543e902fce144c56ad94eecb5d1831b2b64b

####################################################
######## Data insertor for Properties scheme ####
###################################################

<<<<<<< HEAD
    cur = conn.cursor()

    with open('properties_info.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'properties.properties_info', sep=',')

    conn.commit()

    cur = conn.cursor()

    with open('rental_agreement.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'properties.rental_agreement', sep=',')

    conn.commit()
    print("Properties schema data insertion complete...")
=======
cur = conn.cursor()

with open('properties_info.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'properties.properties_info', sep=',')

conn.commit()

cur = conn.cursor()

with open('rental_agreement.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'properties.rental_agreement', sep=',')

conn.commit()
>>>>>>> 3110543e902fce144c56ad94eecb5d1831b2b64b

####################################################
######## Data insertor for Management schema ####
###################################################

<<<<<<< HEAD
    with open('review_info.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'management.review_info', sep=',')

    conn.commit()

    with open('branch_info.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'management.branch_info', sep=',')

    conn.commit()
    

    with open('employee_info.csv', 'r') as f:
        # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'management.employee_info', sep=',')

    conn.commit()
    print("Management schema data insertion complete...")
    print("All insertions successfully completed!")

except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        traceback.print_exc()

finally:
        if conn is not None:
            conn.close()
=======
with open('review_info.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'management.review_info', sep=',')

conn.commit()

with open('branch_info.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'management.branch_info', sep=',')

conn.commit()

with open('employee_info.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'management.employee_info', sep=',')

conn.commit()
>>>>>>> 3110543e902fce144c56ad94eecb5d1831b2b64b
