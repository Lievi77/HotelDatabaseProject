# Project for CSI2132: Hotel Management Database Project

# Things to do

+ Develop the UI (basic, no need for fancy things unless you have time). [Chris] {IN PROGRESS}

+ Create Schemas [Lev] {DONE}

+ Create Tables and Constrains. [Lev] {DONE}

+ Review Project and make sure tables satisfy **all** requirements. {DONE}

+ **LAST MINUTE CHANGE** Will try to generate random data to populate the tables {DONE}

+ Populate Tables [Lev]{FINAL CHECK OF THE SCHEMA BEFORE INSERTION IN PROGRESS} 

- Do the specified Queries [Chris]

- Begin report. [Chris + Lev] (Lev will type the final report on Latex)

# Database Development Log

4 schemas in total: users, management, trasactions, properties

## Users Schema

- AccountID, Name, LastName, phone number,city and country Cannot be null for "user" table.

- AccountID is a foreign key on user, host and guest tables. 

- Created the user_info, host and guest Table (added constraints).

## Management Schema

- Created Management schema tables: branch_info & info_table.

- Added a column in branch_info table: branch_id. Must be unique.

- Constraint for num_employees: must be positive and greater than zero.

- For employee_info table: added a new column that relates a worker to its working branch: "works_for_branch_id" it cannot be null.

- Noticed that we are missing a "Review" entity. It will have the following columns: review_id (pkey) ,reviewed_property_id (fkey) , reviewer_id (fkey), review_text and number_of_stars (between 1 and 5).

## Transaction Schema

- For payment_info table: added a foreign key called host_collector_id and has_been_collected (need to add constraints on type of payment, payment status)

- For Pricing Table: added property_priced_id column (need to add foreign key referencing property_id) and changed amenities to star_amenity (to simplify work).

## Properties Schema

- Created a rental_agreement table. Added contract_id column (pkey and unique), property_id (property on which this agreement is linked to), guest_signee_id (references to guest.guest_id), host_grantor_id (references to host.host_id) and payment_id (need to define the foreign constraint for this though).

- Created a property_table, removed a column called "room type". Added number_of rooms, owner_id (host id fkey) and is_occupied columns with their appropiate constraints.

**FINAL CHECK IS COMPLETED**

# UI Development Log

- [...]


# Report Draft

- Languages used: SQL PostgreSQL flavour and Python.

### Installation of Database Instructions

1. Restore the provided Database Backup (CSI2132PROJECTLEVCHRIS) using pgAdmin 4. The backup will only contain the
schemas and skeleton tables with no data.

2. Execute the provided data generator script (data_generator.py) to generate the data to be inserted. 

3. Execute the insertion script (data_insertor.py) to insert the data into the database.

4. [UI INSTRUCTIONS HERE]

...

...

...

...
