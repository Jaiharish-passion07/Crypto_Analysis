import psycopg2
import psycopg2.extras


def create_table(table_name):
    try:
        conn = None

        with psycopg2.connect(
                database="#####",
                user='#####',
                password='#####',
                host='#####',
                port='#####') as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                # call a stored procedure
                cur.execute('''CALL pr_create_tables(%s)''',(table_name,))

                print(f"The Table {table_name} is created successfully into Crpyto Database")

    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_table(table_name,insert_values):
    try:
        conn = None

        with psycopg2.connect(
                database="#####",
                user='#####',
                password='#####',
                host='#####',
                port='#####') as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                if table_name == "top_100_coins":
                    # Insert elements into DB
                    for data in insert_values:
                        cur.execute('''CALL Insert_values_top_100(%s,%s,%s,%s,%s,%s,%s)''',
                                    (data[0], data[1], data[2], data[3], data[4], data[5], table_name,))
                    print(f"The Data is written successfully into the Table {table_name} ..")
                else:
                    pass
                    for data in insert_values:
                        cur.execute('''CALL Insert_values_alt_coins(%s,%s,%s,%s,%s,%s,%s,%s)''', (data[0],data[1],data[2],data[3],data[4],data[5],data[6],table_name,))
                    print(f"The Data is written successfully into the Table {table_name} ..")


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
