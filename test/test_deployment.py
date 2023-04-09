import pytest
import time

import sys
sys.path.append("../framework")

from framework.create_object import *
from framework.teardown_object import *

# @pytest.fixture(scope='module')
# def deploy_prep():
#     print('----------setup------------')
#     create_objects()
#     print('----------teardown------------')
#     drop_objects()

def test_deployment():
    create_objects()
    time.sleep(5)

    cxn_cursor = connect()
    cxn_cursor.execute("USE DATABASE myDb2;")
    cxn_cursor.execute("USE SCHEMA myDb2.mySchema;")
    cxn_cursor.execute("USE WAREHOUSE WH;")

    row_ans = cxn_cursor.execute("select * from myDb2.mySchema.myTable")
    rows = row_ans.fetchall()

    drop_objects()

    test_result = ''

    if len(rows)==2:
        test_result = 'Pass'
    else:
        test_result = 'Fail'

    assert test_result == 'Pass'



