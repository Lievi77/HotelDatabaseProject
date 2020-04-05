# written by Lev C. Guzman Aparicio 300038033 lguzm038@uottawa.ca 2020
import csv
import psycopg2

################################################
# script that inserts data recorded in csv files
###############################################
# connection setup

conn = psycopg2.connect("host= localhost dbname= project user = postgres password = cherokee77")


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

