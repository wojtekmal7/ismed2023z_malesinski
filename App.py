from BloodTest import BloodTest
import json


def show(a):
    """
    Prints all attributes of all BloodTest objects in the list
    :param a: Is the list of BloodTest objects
    :return: None
    """
    for i in range(len(a)):
        print(f"Pesel: {a[i].pesel_nr}\n"
              f"Name: {a[i].first_name}\n"
              f"Surname: {a[i].last_name}\n"
              f"Number of erythrocytes: {a[i].erythrocytes_nr}\n"
              f"Number of leukocytes: {a[i].leukocytes_nr}\n"
              f"Number of platelets: {a[i].platelets_nr}\n")


def write(filename, a):
    """
    Saves data to txt file
    :param filename: Name of the file
    :param a: Is the list of BloodTest objects
    :return: None
    """
    g = []
    for i in range(len(a)):
        g.append(str(a[i]))
    with open(filename, "wt", encoding="utf-8") as file:
        json.dump(g, file, indent=len(g))


def add(a):
    """
    A function that allows to determine the values of the attributes of the BloodTest class object
    by entering them on the screen
    :param a: Is the list of BloodTest objects
    :return: None
    """
    erythrocytes_nr = None
    leukocytes_nr = None
    platelets_nr = None
    pesel_nr = None
    first_name = input("Enter the patient's name: ")
    last_name = input("Enter the patient's surname: ")
    while pesel_nr is None:
        b = input("Enter the patient's pesel: ")
        if pesel(b):
            pesel_nr = b
        else:
            print("No valid value provided\nWe would like to remind you that the PESEL consists of 11 digits")
    while erythrocytes_nr is None:
        erythrocytes = input("Enter the number of erythrocytes: ")
        erythrocytes_nr = ifint2(erythrocytes)
    while leukocytes_nr is None:
        leukocytes = input("Enter the number of leukocytes: ")
        leukocytes_nr = ifint2(leukocytes)
    while platelets_nr is None:
        platelets = input("Enter the number of platelets: ")
        platelets_nr = ifint2(platelets)
    a.append(BloodTest(first_name, last_name, pesel_nr, erythrocytes_nr, leukocytes_nr, platelets_nr))


def read(filename, o):
    """
    Read data from txt file
    :param filename: Name of the file
    :param o: Is the list of BloodTest objects
    :return: None
    """
    with open(filename, "rt", encoding="utf-8") as file:
        c = json.loads(file.read())
    for i in range(len(c)):
        a = str(c[i])
        b = a.split(" ")
        if pesel(b[0]):
            pesel_nr = b[0]
        else:
            print("The file contains an incorrect value for the PESEL number")
            return
        first_name = b[1]
        last_name = b[2]
        erythrocytes_nr = ifint2(b[3])
        if erythrocytes_nr is None:
            print("The file contains an incorrect value for the erythrocytes number")
            return
        leukocytes_nr = ifint2(b[4])
        if leukocytes_nr is None:
            print("The file contains an incorrect value for the leukocytes number")
            return
        platelets_nr = ifint2(b[5])
        if platelets_nr is None:
            print("The file contains an incorrect value for the platelets number")
            return
        o.append(BloodTest(first_name, last_name, pesel_nr, erythrocytes_nr, leukocytes_nr, platelets_nr))


def eq(pesel, b):
    """
    A function that searches for objects with a given PESEL number and prints them
    :param pesel: It's given PESEL number
    :param b: Is the list of BloodTest objects
    :return: None
    """
    for i in range(len(b)):
        p = 0
        if b[i].pesel_nr == pesel:
            g = [b[i]]
            show(g)
            p = 1
    if p == 0:
        print("Patient with that pesel is not exist")


def pesel(pesel):
    """
    A function that checks whether the PESEL consists of 11 digits
    :param pesel: It's the given PESEL value which is being checked
    :return: TRUE when PESEL number is correct and FALSE when is not
    """
    a = 1
    try:
        b = int(pesel)
    except ValueError:
        a = 0
    return len(pesel) == 11 and a == 1


def ifint(something):
    """
    A function that checks whether the given value can be written as an int
    :param something: Given value
    :return: TRUE when the given object can be written as an int and FALSE when it cannot
    """
    a = 1
    try:
        b = int(something)
    except ValueError:
        a = 0
    return a == 1


def ifint2(value):
    """
    A function that returns a given value if it can be written as an int, or prints a message to the screen if it cannot
    :param value: Given value
    :return: given value or None
    """
    if ifint(value):
        return value
    else:
        print("No valid value provided")
        return


def delete(pesel, b):
    """
    A function that deletes test results of patient by given number
    :param pesel: It's the given PESEL number
    :param b: Is the list of BloodTest objects
    :return: None
    """
    a = 0
    c = []
    while a == 0:
        doornot2 = 0
        doornot3 = 0
        try:
            for i in range(len(b)):
                p = 0
                if b[i].pesel_nr == pesel:
                    g = [b[i]]
                    show(g)
                    p = 1
            if p == 0:
                print("Patient with that pesel is not exist")
            for i in range(len(b)):
                if b[i].pesel_nr == pesel:
                    c.append(i)
            if len(c) > 0:
                while doornot2 == 0:
                    d = int(input("Which test you want to "
                                  "remove(for example 2 is second test on the list on the screen): "))
                    if d < 1:
                        print("You must enter the number greater than zero")
                    else:
                        try:
                            doornot2 = 1
                            y = c[d - 1]
                        except IndexError:
                            print("There's no so many choices!")
                            doornot2 = 0
                del b[c[d - 1]]
                if len(c) > 1:
                    c.clear()
                    while doornot3 == 0:
                        e = int(input("Do you want do remove more data? 1-yes,0-no"))
                        if e == 0:
                            doornot3 = 1
                            a = 1
                        elif e == 1:
                            doornot3 = 1
                            a = 0
                        else:
                            print("You can enter only 1 or 0!")
                else:
                    a = 1
            else:
                a = 1
        except ValueError:
            print("It's not a number")
