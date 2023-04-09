import sys
sys.path.append("../lib")

from lib.snowflake_connector import *

def create_sp_func():
    try:
        cxn_cursor = connect()

        cxn_cursor.execute("USE DATABASE myDb2;")
        cxn_cursor.execute("USE SCHEMA myDb2.mySchema;")
        cxn_cursor.execute("USE WAREHOUSE WH;")

        sql_command="""CREATE OR REPLACE PROCEDURE UPPER_CASE_COLUMN_PY(table_name VARCHAR, column_name VARCHAR)
                    RETURNS STRING
                    LANGUAGE PYTHON
                    RUNTIME_VERSION = '3.8'
                    PACKAGES = ('snowflake-snowpark-python')
                    HANDLER = 'run'
                    AS 
                    $$def run(session, table_name, column_name):
                        session.sql(f"UPDATE {table_name} SET {column_name} = UPPER({column_name});").collect()
                        return f'Function deployed successfully.'$$;"""

        # sql_command="""select * from myDb2.mySchema.myTable"""

        cxn_cursor.execute(sql_command)

        print("Function created successfully.")

    except ProgrammingError as e:
        print("An error occurred while trying to establish a connection:", e)