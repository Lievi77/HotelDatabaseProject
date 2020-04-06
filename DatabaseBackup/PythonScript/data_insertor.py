# written by Lev C. Guzman Aparicio 300038033 lguzm038@uottawa.ca 2020
import psycopg2

################################################
# script that inserts data recorded in csv files
###############################################
# connection setup

conn = psycopg2.connect("host= web0.eecs.uottawa.ca dbname= lguzm038 user = lguzm038 password = Kyorzkyre77! port = 15432")


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
