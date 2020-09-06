import psycopg2 as pg2

try:
    conn = pg2.connect(
    host="127.0.0.1", 
    port="5434",
    database="dvdrental",
    user="postgres",
    password=""
    )

    #cursor
    #Print PostgreSQL Connection properties
    cur = conn.cursor()
    print ( conn.get_dsn_parameters(),"\n")

    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("You are connected to - ", record,"\n")

    cur.execute("INSERT INTO actor (first_name,last_name,last_update) VALUES ('Manuel', 'Varela', CURRENT_TIMESTAMP)")

    cur.execute("SELECT first_name,last_name FROM actor")
    rows = cur.fetchmany(10)

    for r in rows:
       print(f"first_name {r[0]} last_name {r[1]}")
    #print(rows)

    cur.execute("SELECT * FROM payment")
    payment= cur.fetchone()
    print(payment)

    #cur.fetchone() it returns the first row of data.
    #cur.fetchmany(10) it returns how many rows you put in the parameters
    #cur.fetchall() it returns all rows from the table

    conn.commit()

except (Exception, pg2.Error) as error:
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(conn):
            cur.close()
            conn.close()
            print("PostgreSQL connection closed")



