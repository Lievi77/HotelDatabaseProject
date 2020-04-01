#written by Lev C. Guzman Aparicio 300038033 lguzm038@uottawa.ca 2020
import csv
import psycopg2

#connection setup

conn = psycopg2.connect("host= localhost dbname= project user = postgres password = cherokee77")

########## Population of users schema ################

#cursor for populating user_info table
cur = conn.cursor()


#cursor for populating guest_info table



#cursor for populating host_info table


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
