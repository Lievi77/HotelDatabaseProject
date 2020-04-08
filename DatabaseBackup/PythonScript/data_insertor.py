# written by Lev C. Guzman Aparicio 300038033 lguzm038@uottawa.ca 2020
import psycopg2
import traceback

################################################
# script that inserts data recorded in csv files
###############################################

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

####################################################
######## Data insertor for TRANSACTIONS scheme ####
###################################################

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

####################################################
######## Data insertor for Properties scheme ####
###################################################

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

####################################################
######## Data insertor for Management schema ####
###################################################

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
