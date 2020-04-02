#written by Lev C. Guzman Aparicio 300038033 lguzm038@uottawa.ca 2020
import csv
import psycopg2

#connection setup

conn = psycopg2.connect("host= localhost dbname= project user = postgres password = cherokee77")

########## Population of users schema ################

#cursor for populating user_info, host_info and guest_info table
# insertion in user_info, guarantees population of the other two

cur = conn.cursor()

with open('user_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        #must follow schema format
        row
        )

conn.commit()

############ Population of transactions schema ################

#cursor for populating transaction_info table 


#cursor for populating the pricing table


############ Population of properties schema ################

#cursor for populating properties_info table


#cursor for populating rental_agreement table


############ Population of management schema ################

# cursor for populating branch_info table


#cursor for populating employee_info table



#cursor for populating review_info table
