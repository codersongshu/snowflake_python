import sys
sys.path.append("../lib")

from lib.snowflake_connector import *

def drop_objects():
    try:
        cxn_cursor = connect()

        # cxn_cursor.execute("SELECT current_version()")
        # one_row = cxn_cursor.fetchone()
        # print(one_row[0])
        # print("Connection established successfully.")

        cxn_cursor.execute("DROP DATABASE myDb2;")
        cxn_cursor.execute("DROP WAREHOUSE WH;")

        print("Objects dropped successfully.")

        cxn_cursor.close()

        # row_ans = cxn_cursor.execute("select * from myDb.mySchema.myTable")
        # rows = row_ans.fetchall()
        #
        # for row in rows:
        #     print('-------------')
        #     print(row[0])
        #     print('-------------')
        #     print(row[1])
        #     print('-------------')
        #     print(row)

    except ProgrammingError as e:
        print("An error occurred while trying to establish a connection:", e)

