from config import *
import snowflake.connector
from snowflake.connector import ProgrammingError

config = get_config()

def connect():
    # config_dict = config.get_config()
    # print(config.get_config())
    cxn = snowflake.connector.connect(
        user=config['user'],
        password=config['password'],
        account=config['account'],
        warehouse=config['warehouse'],
        database=config['database'],
        schema=config['schema']
    )

    # print(config.get_config())

    cxn_cursor = cxn.cursor()
    return cxn_cursor
    # try:
    #     cxn_cursor.execute("SELECT current_version()")
    #     one_row = cxn_cursor.fetchone()
    #     print(one_row[0])
    #     print("Connection established successfully.")
    #
    #     cxn_cursor.execute("CREATE OR REPLACE DATABASE myDb2;")
    #     cxn_cursor.execute("CREATE OR REPLACE SCHEMA myDb2.mySchema")
    #     cxn_cursor.execute("CREATE OR REPLACE TABLE myDb2.mySchema.myTable(id number,name varchar);")
    #     cxn_cursor.execute("USE WAREHOUSE WH;")
    #
    #     cxn_cursor.execute("insert into myDb2.mySchema.myTable(id, name) VALUES (1,'John'),(2,'Mat');")
    #
    #     row_ans = cxn_cursor.execute("select * from myDb.mySchema.myTable")
    #     rows = row_ans.fetchall()
    #
    #     for row in rows:
    #         print('-------------')
    #         print(row[0])
    #         print('-------------')
    #         print(row[1])
    #         print('-------------')
    #         print(row)
    #
    # except ProgrammingError as e:
    #     print("An error occurred while trying to establish a connection:", e)



