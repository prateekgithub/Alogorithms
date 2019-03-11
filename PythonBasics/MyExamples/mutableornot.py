#!/usr/bin/env python3
try:
    myStr = input("Enter a data: ")
    evalStr = eval(myStr)
    oldId = id(evalStr)
    print(oldId)
    if isinstance(evalStr, int):
        print(f'Input type {myStr} is Integer')
        evalStr = evalStr + 1
        newId = id(evalStr)
    elif isinstance(evalStr, list):
        print(f'Input type {myStr} is List')
        evalStr.append(3)
        newId = id(evalStr)
    elif isinstance(evalStr, range): print(f'Input type {myStr} is Range')
    elif isinstance(evalStr, dict): print(f'Input type {myStr} is Dictionary')
    elif isinstance(evalStr, set): print(f'Input type {myStr} is Set')
    elif isinstance(evalStr, tuple): print(f'Input type {myStr} is Tuple')
    else:
        print("Unknown Input")
    if oldId == newId:
        print(f'Input type {myStr} is mutable with old id - {oldId} and new id - {newId}')
    else:
        print(f'Input type {myStr} is immutable with old id - {oldId} and new id - {newId}')
except Exception as err:
    if (type(err) == NameError) and (str(err) == "name '{}' is not defined".format(myStr)):
        print(f'Input type {myStr} is String')
    else:
        print("Unknown Type with error: {}".format(err))
