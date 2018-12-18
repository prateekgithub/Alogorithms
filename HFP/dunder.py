#!/usr/bin/env python3

'''
When the Python interpreter reads a source file, it executes all of the code found in it.

Before executing the code, it will define a few special variables.
For example, if the Python interpreter is running that module (the source file) as the main program, 
it sets the special __name__ variable to have a value "__main__". 
If this file is being imported from another module, __name__ will be set to the module's name.

Ex:
python dunder.py
on the command line. After setting up the special variables, it will execute the import statement and load those modules. 
It will then evaluate the def block, creating a function object and creating a variable called myfunction 
that points to the function object. It will then read the if statement and see that 
__name__ does equal "__main__", so it will execute the block shown there.

One reason for doing this is that sometimes you write a module (a .py file) where it can be executed directly. 
Alternatively, it can also be imported and used in another module. 
By doing the main check, you can have that code only execute when you want to run the module as a program 
and not have it execute when someone just wants to import your module and call your functions themselves.'''


print('We start off in:',__name__)
if __name__=='__main__':
    print('And end up in:',__name__)