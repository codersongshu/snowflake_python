import sys
sys.path.append("../framework")

import time

from framework.create_object import *
from framework.teardown_object import *
from framework.create_sp_function import *


create_objects()

time.sleep(5)

create_sp_func()

time.sleep(5)

# cxn_cursor = connect()
# cxn_cursor.execute("USE DATABASE myDb2;")
# cxn_cursor.execute("USE SCHEMA myDb2.mySchema;")
# cxn_cursor.execute("USE WAREHOUSE WH;")
#
# row_ans = cxn_cursor.execute("select * from myDb2.mySchema.myTable")
# rows = row_ans.fetchall()
#
# for row in rows:
#     print('-------------')
#     print(row[0])
#     print('-------------')
#     print(row[1])
#     print('-------------')
#     print(row)

drop_objects()