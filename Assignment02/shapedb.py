# Assignment 02 - Shape Database
# Naika Jean-Baptiste (40227367)
# COMP 348 - SUMMER 2023

from multiset import *


def loadFile():
    filename = input("Enter the name of the database file: ")
    file = open(filename, "rt")
    current_shape = file.readline()




def to_set():
    pass


def handle_choice(choice):
    if choice == 1:
        loadFile()
    elif choice == 2:
        to_set()
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        pass


# def handleOps(args, n):
#     for i in range(1, n):
#         if args[i].lower() == 'load':
#             print("Loading file: ")
#             loadFile()
#         elif args[i].lower() == 'toset':
#             print("Converting to set: ")
#         elif (args[i].lower() == 'save'):
#             print("Saving file: ")
#         elif (args[i].lower() == 'print'):
#             print("Printing file: ")
#         elif (args[i].lower() == 'summary'):
#             print("Printing summary: ")
#         elif (args[i].lower() == 'details'):
#             print("Printing details: ")
#         elif (args[i].lower() == 'quit'):
#             print("Quitting program")
#             return
#         else:
#             print("Invalid argument: " + args[i])
#             return
#

def main():
    print("Welcome to the Shape Database. Please enter a choice (1-7) from the options below:\n"
          + "\t1.LOAD\n\t2.TOSET\n\t3.SAVE\n\t4.PRINT\n\t5.SUMMARY\n\t6.DETAILS\n\t7.QUIT")

    choice = input("Choice: ")
    handle_choice(choice)
    print("Option chosen: " + choice)


if __name__ == "__main__":
    main()
