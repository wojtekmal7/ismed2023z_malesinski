import App
import os


def main():
    """
    Menu allowing communication with the user
    :return: None
    """
    tmp = []
    while True:
        try:
            choice = int(input("Choose:\n1 - new study\n2 - list all tests currently loaded in the system"
                               "\n3 - save the results to a file\n4 - load results from file"
                               "\n5 - search for a patient by PESEL number\n"
                               "6 - delete tests currently loaded on the system"
                               "\n7 - exit the program\nYour choice: "))
        except ValueError:
            print("No number given")
        try:
            if choice == 1:
                App.add(tmp)
            elif choice == 2:
                App.show(tmp)
            elif choice == 3:
                try:
                    path = input("Provide the location of the folder where you want to save the file: ")
                    os.chdir(path)
                    filename1 = input("Enter a file name: ")
                    filename2 = filename1 + ".json"
                    try:
                        App.write(filename2, tmp)
                    except FileNotFoundError as error:
                        print(error)
                except PermissionError:
                    print("You do not have permission to save the file here")
                except FileNotFoundError:
                    print("There is no such folder!\nSelect an existing folder")
            elif choice == 4:
                try:
                    path = input("Enter the location of the folder "
                                 "where the file whose data you want to load is located: ")
                    os.chdir(path)
                    filename1 = input("Enter a file name: ")
                    filename2 = filename1 + ".json"
                    try:
                        App.read(filename2, tmp)
                    except FileNotFoundError:
                        print("Such a file does not exist!\nSelect an existing file")
                except PermissionError:
                    print("You do not have permission to save the file here")
                except FileNotFoundError:
                    print("There is no such folder!\nSelect an existing folder")
                except OSError as error:
                    print(error)
            elif choice == 5:
                doornot3 = 1
                while doornot3 == 1:
                    a = input("Enter the PESEL number of the patient you are looking for: ")
                    if App.pesel(a):
                        App.eq(a, tmp)
                        doornot3 = 0
                    else:
                        print("No valid value provided\n"
                              "We would like to remind you that the PESEL consists of 11 digits")
            elif choice == 6:
                doornot = 1
                while doornot == 1:
                    a = input("Enter the PESEL number of the patient test you want to remove: ")
                    if App.pesel(a):
                        App.delete(a, tmp)
                        doornot = 0
                    else:
                        print("No valid value provided\n"
                              "We would like to remind you that the PESEL consists of 11 digits")
            elif choice == 7:
                exit()
            else:
                print("Enter a number from 1 to 7")
        except UnboundLocalError:
            print("Enter a number from 1 to 7")


if __name__ == '__main__':
    main()
