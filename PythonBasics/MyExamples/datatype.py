#!/usr/bin/env python3
import sys
#dType = input("Enter a data type: ")
try:
    myStr = input("Enter a data: ")
    evalStr = eval(myStr)
    if isinstance(evalStr, int): print(f'Input type {myStr} is Integer')
    elif isinstance(evalStr, list): print(f'Input type {myStr} is List')
    elif isinstance(evalStr, range): print(f'Input type {myStr} is Range')
    elif isinstance(evalStr, dict): print(f'Input type {myStr} is Dictionary')
    elif isinstance(evalStr, set): print(f'Input type {myStr} is Set')
    elif isinstance(evalStr, tuple): print(f'Input type {myStr} is Tuple')
except Exception as err:
    if (type(err) == NameError) and (str(err) == "name '{}' is not defined".format(myStr)):
        print(f'Input type {myStr} is String')
    else:
        print("Unknown Type with error: {}".format(err))
