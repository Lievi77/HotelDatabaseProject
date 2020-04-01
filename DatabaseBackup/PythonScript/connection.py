import csv
import psycopg2

conn = psycopg2.connect("host= localhost dbname= project user = postgres password = cherokee77")

#cursor for populating user_info table
cur = conn.cursor()
with open('bnb_NewYork_2019.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO users VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s)",
        row
        )
conn.commit()

#cursor for populating guest_info table



#cursor for populating host_info table



