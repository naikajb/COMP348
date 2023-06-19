# Assignment 02 - Shape Database
# Naika Jean-Baptiste (40227367)
# COMP 348 - SUMMER 2023

from shapes import *

shape_list = []


def handle_shape(line):
    line = line.strip().split()

    if "shape" in line[0]:
        if len(line) > 1:
            return 0
        shape = Shape()
        shape_list.append(shape)
        return 1

    elif "rhombus" in line[0]:
        if int(line[1]) < 0 or int(line[2]) < 0:
            return 0
        else:
            r = Rhombus(int(line[1]), int(line[2])) 
            shape_list.append(r)
            return 1
        # # print(shapes_mltst)
        #print("rhombus found: " + line)

    elif "circle" in line[0]:
        c = Circle(int(line[1]))
        shape_list.append(c)
        #print("circle found: " + line)
        return 1

    elif "ellipse" in line[0]:
        if int(line[1]) < 0 or int(line[2]) < 0:
            return 0
        e = Ellipse(int(line[1]), int(line[2]))
        shape_list.append(e)
        return 1
        #print('ellipse found: ' + line)


def loadFile():
    filename = "ShapeDatabase.txt"
    file = open(filename, "r")
    print("Processing " + file.name + "...\n")

    rows = 0
    valid = 0
    error = 0
    for line in file:
        rows += 1
        valid += handle_shape(line)
        error = rows - valid
    file.close()

    print("Processed " + str(rows) + " row(s), " + str(valid) + " shapes were loaded, " + str(error) + " error(s).\n")
    for shape in shape_list:
        shape.print()


def to_set():
    print(shape_list.pop)
    pass


def print_set():
    print("Shapes in the database:\n")
    for shape in shape_list:
        shape.print()


def handle_choice(choice):
    if choice == "1":
        loadFile()
    elif choice == "2":
        to_set()
    elif choice == "3":
        pass
    elif choice == "4":
        pass
        # print_set()
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        pass



def main():

    choice = 1

    while choice != "7":
        print("Welcome to the Shape Database. Please enter a choice (1-7) from the options below:\n"
          + "\t1.LOAD\n\t2.TOSET\n\t3.SAVE\n\t4.PRINT\n\t5.SUMMARY\n\t6.DETAILS\n\t7.QUIT")

        choice = input("Choice: ")
        handle_choice(choice)
        # print("Option chosen: " + choice + "\n")
        # for shape in shape_list:
            
        #     shape.print()
    
    print("Thank you for using the Shape Database. Goodbye!")
    # test = shape_list.pop()
    # print(test.area())

if __name__ == "__main__":
    main()
