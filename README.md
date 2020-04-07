# Project for CSI2132: Hotel Management Database Project

# Things to do

+ Develop the UI (basic, no need for fancy things unless you have time). [Chris] {IN PROGRESS}

+ Create Schemas [Lev] {DONE}

+ Create Tables and Constrains. [Lev] {DONE}

+ Review Project and make sure tables satisfy **all** requirements. {DONE}

+ **LAST MINUTE CHANGE** Will try to generate random data to populate the tables {DONE}

+ Populate Tables [Lev]{DONE} 

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


1. Execute the insertion script (data_insertor.py) to insert the data into the database.

3. Database set up.

4. [UI INSTRUCTIONS HERE]

 To install the CLI tool it is ***important*** that the guide is followed in order to make sure that no errors present themselves
 
 - It is *strongly* advised that the program is ran in a virtual environment
 - It is ***even more so*** advised that it is run using the latest version of Python, but any Python 3.X version will suffice,
   please **do not use** Python 2.X binaries because there ***WILL*** be errors
 - Once in a virtual environment run the command:
    ` pip install --editable .`   
        What this is essentially telling Python is to install the package in the current directory (which you guessed it, is our CLI Tool), the editable option will link the package to the directory location and mitigate any nasty import errors.
        
  - If on a UNIX system you might have to run the following instead:
    `pip3 install --editable .` 
        This specifies to your system to select a Python 3.X version if a Python 2.X is also installed (which is usally the case with Linux distros)
  
  - Once installed verify installation by checking for the package `travelCLI   v1.0`
      Type in `pip list` or `pip3 list` (if on a UNIX system)
   
   - To finally start using the CLI Tool, the binding keyword is `controller` so if I were to run the check command I would do like so:
   `$ controller check` 
   
   Note that you will need to edit the configuration file titled `database.ini` to change the credentials to appropriate ones
...

...

...
