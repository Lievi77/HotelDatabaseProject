# Project for CSI2132 :Hotel Database Project


# Things to do

+ Develop the UI (basic, no need for fancy things unless you have time). [Chris] {IN PROGRESS}

+ Create Schemas [Lev] {DONE}

+ Create Tables and Constrains. [Lev] {IN PROGRESS}

+ Search for data sets to populate tables. [Chris] (hint: use Kaggle or any free data source) {2/2 COMPLETE}

+ Populate Tables [Lev]{Will try to get this done by friday or thursday}

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

## Transaction Schema

- For payment_info table: added a foreign key called host_collector_id and has_been_collected (need to add constraints on type of payment, payment status)

- For Pricing Table: added property_priced_id column (need to add foreign key referencing property_id) and changed amenities to star_amenity (to simplify work).

## Properties Schema

-

# Report Draft

- Languages used: SQL PostgreSQL flavour and [Python?]

...

...

...

...
