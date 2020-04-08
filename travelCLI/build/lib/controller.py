import click, psycopg2, os
from psycopg2 import sql
from colorama import init, Fore, Back, Style
from .config import config



@click.group()

def session():
    pass

@session.command()
def check():
    """ Check connection status to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
      
        # create a cursor
        cur = conn.cursor()
        
   # execute a statement
        click.secho('PostgreSQL database version:', fg='yellow')
        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
       # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            click.secho('Database connection closed.', fg='yellow')

@session.command()
@click.argument('property_id',type=int)
@click.argument('rentaltype', type=str)
@click.argument('rooms', type=int)
@click.argument('owner_id',type=int)
@click.argument('available_date',type=str)
@click.argument('pricing_id', type=int)
@click.argument('location',type=str)
def insertlisting(property_id,rentaltype,rooms,owner_id, available_date, pricing_id, location):
    "Insert a new property listing into the database"

    try:

        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        #the SQL query is nested into the execute statement
        #format for date is YY-MM-DD
        cur.execute(sql.SQL("SET search_path= properties; INSERT INTO {} VALUES (%s, %s, %s, %s, %s, %s, %s)").
        format(sql.Identifier('properties_info')),(property_id, rentaltype, rooms, owner_id, available_date, pricing_id, location))
        conn.commit()
        click.secho("Your listing has been posted!", fg='yellow')
        cur.close

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        click.secho("Unfortunately, the listing was not posted!", fg='yellow')

    finally:
        if conn is not None:
            conn.close()
        

@session.command()
def showlistings():
    "Displays all available property listings in the database"

    query = sql.SQL("SET search_path= properties; SELECT * FROM {table}").format(
        table = sql.Identifier('properties_info'))
    
    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            click.secho()
            click.secho(print("Property ID:", str(row[0])))
            click.secho(print("Rental Type:", str(row[1])))
            click.secho(print("Number of Rooms", str(row[2])))
            click.secho(print("Owner ID:", str(row[3])))
            click.secho(print("Available Date:", str(row[4])))
            click.secho(print("Pricing ID:", str(row[5])))
            click.secho(print("Location:", str(row[6])))
            click.secho("-----------------------------------------------", fg='green')

        click.secho("Displayed above are all the current listings!", fg='yellow')
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        click.secho("Unfortunately, the listing cannot be displayed!", fg='yellow')

    finally: 
        if conn is not None:
            conn.close()

@session.command()
def showrates():
    "Shows the different rates available for properties"
    query = sql.SQL("SET search_path = transactions; SELECT {field} FROM {table}").format(
        table = sql.Identifier('pricing'),
        field = sql.Identifier('pricing_id'))

    try:
        conn = None
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(query)
        row = cur.fetchall()

        click.secho("There are listings available at the price of:",fg='yellow')
        for items in row:
            click.secho("$ {}".format(items), fg='green', bold=True)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        click.secho("Unfortunately, the pricings could not be fetched!", fg='yellow')

    finally: 
        if conn is not None:
            conn.close()
            
