# **********************************
# if __name__ == '__main__'
# **********************************

# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# with the help of if __name__ == '__main__'
# we can check that our module is running as standalone program
# or as a imported module by another module

# python interpreter sets "special  variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run


print(__name__)


# if i import this module to another file and print
# the print(module.__name__) this will return the module name not main


if __name__ == '__main__':
    print('running this module directly')  # runing as a standalone
else:
    print('running other module indirectly')  # running as a imported module


# def main():
#     pass

# if __name__ == '__main__':
#     main()
