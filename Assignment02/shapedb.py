# Assignment 02 - Shape Database
# Naika Jean-Baptiste (40227367)
# COMP 348 - SUMMER 2023

from shapes import *

shape_list = [] # original multi set implemented as a list of tuples with each shapes info and id
setified = False # flag to indicate if the multi set has been converted to a set
loaded = False # flag to indicate if the file has been loaded
shape_set = set() # setified multi set

def handle_shape(line):
    line = line.strip().split()

    if "shape" in line[0]:
        if len(line) > 1:
            return 0
        else:
            s = Shape()
            shape_list.append((s, ""))
            # shape_list.append((s, s.id))
            return 1

    elif "rhombus" in line[0]:
        if int(line[1]) < 0 or int(line[2]) < 0:
            return 0
        else:
            r = Rhombus(int(line[1]), int(line[2])) 
            shape_list.append((r, r.d1, r.d2))
            # shape_list.append((r, r.id, r.d1, r.d2))
            return 1
        # # print(shapes_mltst)
        #print("rhombus found: " + line)

    elif "circle" in line[0]:
        if int(line[1]) < 0:
            return 0
        else: 
            c = Circle(int(line[1]))
            shape_list.append((c, int(line[1])))
            # shape_list.append((c, c.id, int(line[1])))
            #print("circle found: " + line)
            return 1

    elif "ellipse" in line[0]:
        if int(line[1]) < 0 or int(line[2]) < 0:
            return 0
        else:
            e = Ellipse(int(line[1]), int(line[2]))
            shape_list.append((e, int(line[1]), int(line[2])))
            # shape_list.append((e, e.id, int(line[1]), int(line[2])))
            return 1
        #print('ellipse found: ' + line)


def loadFile():
    global loaded
    filename = input("\n\tPlease enter the name of the file you want to load: ")
    if filename == "":
        print("\n\tError: No such file in directory.\n")
        return
    else:
        loaded = True
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
    if loaded == False:
        print("\n\tError: File not loaded.\n")
        return
    global setified 
    setified= True
    for shape in shape_list:
        t = ""
        shape_tuple = ()

        for x in range(len(shape)):
            if x == 0:
                t = shape[x]
            else:
                t = str(shape[x])
                y = list(shape_tuple)
                y.append(t)
                shape_tuple = tuple(y)
            # print(t)


        # shape_info = (shape[0].__class__.__name__, shape[1])
        shape_set.add(shape_tuple)
        info = ""
        for s in shape_set:
            # print("\t" + str(s))
            info += s[0] + ", "
            #info += s[0].__class__.__name__ + " " + str(s[1]) + "\n"
        # print("{ " + info + " }")
    print("\n\tSucessfully converted loaded shapes to set.\n")


def print_set():
    if loaded == False:
        print("\n\tError: Cannot print anything because no file was load. Load a file first.\n")
        return
    # if setified:
    #     print("\n\tShapes in the database:\n")
    #     for shape in shape_set:
    #         shape[0].print()
    # else:
    print("\n\tShapes in the database:\n")
    for shape in shape_list:
        shape[0].print()



def details():
    if loaded == False:
        print("\n\tError: File not loaded.\n")
        return
    if setified:
        print("Shapes in the database:\n")
        for shape in shape_set:
            info = ""
            for i in range(len(shape)):
                if i == 0:
                    info += "\t" + shape[i].lower()# .__class__.__name__.lower()
                # elif i == 1:
                #     pass
                else:
                    info += " " + str(shape[i])
            print(info)
    else:
        print("Shapes in the database:\n")
        for shape in shape_list:
            info = ""
            for i in range(len(shape)):
                if i == 0:
                    info += "\t"+shape[i].__class__.__name__.lower()
                # elif i == 1:
                #     pass
                else:
                    info += " " + str(shape[i])
            print(info)
        
    pass

def save():
    if loaded == False:
        print("\n\tError: Cannot use this operation. Load a file first.\n")
        return
    
    filename = input("\n\tPlease enter the name of the file you want to save to: ")
    if filename == "":
        print("\n\tError: No filename was entered.\n")
        return
    output = open(filename, "w")
    if setified:
        for shape in shape_set:
            info = ""
            for i in range(len(shape)):
                if i == 0:
                    info += shape[i].lower() 
                else:
                    info += " " + str(shape[i])
            output.write(info + "\n")
    else:
        for shape in shape_list:
            info = ""
            for i in range(len(shape)):
                if i == 0:
                    info += shape[i].__class__.__name__.lower()
                else:
                    info += " " + str(shape[i])
            output.write(info + "\n")
    output.close()
    print("\n\tSuccessfully saved shapes to file" + output.name + "\n")


def summary():
    if loaded == False:
        print("\n\tError: File not loaded.\n")
        return
    print("\n\tSummary of shapes in the database:\n")
    c, e, r, s = 0, 0, 0, 0
    if setified == False:
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
    else:
        for shape in shape_set:
            if shape[0] == "Circle":
                c += 1
                s+= 1
            elif shape[0] == "Ellipse":
                e += 1
                s+= 1
            elif shape[0] == "Rhombus":
                r += 1
                s+= 1
            elif shape[0] == "Shape":
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
        summary()
    elif choice == "6":
        details()
    elif choice == "7":
        pass


def main():

    choice = 1

    while choice != "7":
        print("\nWelcome to the Shape Database. Please enter a choice (1-7) from the options below:\n"
          + "\t1.LOAD (DONE)\n\t2.TOSET (DONE)\n\t3.SAVE (DONE)\n\t4.PRINT\n\t5.SUMMARY (DONE)\n\t6.DETAILS (DONE)\n\t7.QUIT (DONE)\n")

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
