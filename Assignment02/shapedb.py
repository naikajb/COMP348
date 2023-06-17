# Assignment 02 - Shape Database
# Naika Jean-Baptiste (40227367)
# COMP 348 - SUMMER 2023

import sys


def loadFile():
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
    print("Option chosen: " + choice)


if __name__ == "__main__":
    main()
