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
        else:
            s = Shape()
            shape_list.append((s, s.id))
            return 1

    elif "rhombus" in line[0]:
        if int(line[1]) < 0 or int(line[2]) < 0:
            return 0
        else:
            r = Rhombus(int(line[1]), int(line[2])) 
            shape_list.append((r, r.id, r.d1, r.d2))
            return 1
        # # print(shapes_mltst)
        #print("rhombus found: " + line)

    elif "circle" in line[0]:
        if int(line[1]) < 0:
            return 0
        else: 
            c = Circle(int(line[1]))
            shape_list.append((c, c.id, int(line[1])))
            #print("circle found: " + line)
            return 1

    elif "ellipse" in line[0]:
        if int(line[1]) < 0 or int(line[2]) < 0:
            return 0
        else:
            e = Ellipse(int(line[1]), int(line[2]))
            shape_list.append((e, e.id, e.a, e.b))
            return 1
        #print('ellipse found: ' + line)


def loadFile():
    filename = "ShapeDatabase.txt"
    file = open(filename, "r")
    print("\n\tProcessing " + file.name + "...\n")

    rows = 0
    valid = 0
    error = 0
    for line in file:
        rows += 1
        i = handle_shape(line)
        if i == 1:
            valid += 1
        else: 
            error += 1
            print("\t\tError in line " + str(rows) + ": " + line)
        
    file.close()

    print("\n\tProcessed " + str(rows) + " row(s), " + str(valid) + " shapes were loaded, " + str(error) + " error(s).\n")
    # print("Shapes in the database:\n")
    # for shape in shape_list:
    #     print(shape)
    

def to_set():
    print(shape_list.pop)
    pass


def print_set():
    print("Shapes in the database:\n")
    for shape in shape_list:
        print(shape[0])


def summary():
    pass

def details():
    pass

def save():
    output = open("NewShapeDatabase.txt", "w")
    for shape in shape_list:
        output.write(str(shape[0].__class__.__name__) + " " + str(shape[0].id) + " " )


def give_summary():
    print("\n\tSummary of shapes in the database:\n")
    c, e, r, s = 0, 0, 0, 0

    for shape in shape_list:
        if shape[0].__class__.__name__ == "Circle" :
            c += 1
            s+= 1
        elif shape[0].__class__.__name__ == "Ellipse":
            e += 1
            s+= 1
        elif shape[0].__class__.__name__ == "Rhombus":
            r += 1
            s+= 1
        elif shape[0].__class__.__name__ == "Shape":
            s += 1
    
    print("\t\tCircle(s): " + str(c) + "\n\t\tEllipse(s): " + str(e) + "\n\t\tRhombus(es): " + str(r) + "\n\t\tShape(s): " + str(s) + "\n")
def handle_choice(choice):
    if choice == "1":
        loadFile()
    elif choice == "2":
        to_set()
    elif choice == "3":
        save()
    elif choice == "4":
        print_set()
    elif choice == "5":
        give_summary()
    elif choice == "6":
        pass
    elif choice == "7":
        pass



def main():

    choice = 1

    while choice != "7":
        print("\nWelcome to the Shape Database. Please enter a choice (1-7) from the options below:\n"
          + "\t1.LOAD\n\t2.TOSET\n\t3.SAVE\n\t4.PRINT\n\t5.SUMMARY\n\t6.DETAILS\n\t7.QUIT")

        choice = input("Choice: ")
        handle_choice(choice)
        # print("Option chosen: " + choice + "\n")
        # for shape in shape_list:  
        #     shape.print()
    
    print("\nThank you for using the Shape Database. Goodbye!")
    # test = shape_list.pop()
    # print(test.area())

if __name__ == "__main__":
    main()
