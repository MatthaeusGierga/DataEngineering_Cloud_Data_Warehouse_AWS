import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


'''
drop existing tables. 
"drop_table_queries" is getting used in "sql_ueries.py".
'''
def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

'''
create new tables. 
"create_table_queries" is getting used in "sql_ueries.py".
Added a try and except statement.
'''
def create_tables(cur, conn):
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(e)


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()