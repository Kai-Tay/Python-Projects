
#Add
def add():
    #Name
    print("If you would like to go back, type 'back' ")
    name= input("You are now adding a new contact! What is the name? ").lower()
    number = 1
    if name == "back":
        menu()
    else:
        #Contact Number
        while number != 2:
            number = input("Whats the phone number? ")
            if len(number) < 8:
                print("The number is less than 8 digits!")
            elif len(number) > 8:
                print("The number is more than 8 digits!")
            else:
                append_file = open("list.txt", "a")
                append_file.write(name + " " + number + "\n")
                append_file.close()
                print("Added!\n")
                menu()
                break

#Delete
def delete():
    list()
    print("If you would like to go back, type 'back' ")
    delete_name = input("Give the name and number you would like to delete with space in between:  ").lower()
    if delete_name == "back":
        print('\n')
        menu()
    else:
        readdata = open("list.txt", "r")
        readfile = readdata.readlines()

        writedata = open("list.txt", "w")
        for string in readfile:
            if delete_name != string.strip():
                writedata.write(string)

            elif delete_name == string.strip():
                print("Done!\n")
        writedata.close()
        menu()

#Edit
def edit():
    list()
    print("If you would like to go back, type 'back' ")
    selectname=input("Which name would you like to edit?")

#Search
def search():
    d = {}
    with open("list.txt") as l:
        for line in l:
            (key,val) = line.split()
            d[key] = val
    for key, value in d.items():
        print(key, ' : ', value)

    print("If you would like to go back, type 'back' ")
    name = input("Type the name you want to search here: \n").lower()
    if name == "back":
        print('\n')
        menu()
    else:
        if name in d:
            print(name + ": " + d[name])
            input("To continue, press enter: \n")
            menu()

        else:
            print("Error!\n")
            menu()

#List SHOWING ALL CONTACTS
def list():
    d = {}
    with open("list.txt") as l:
        for line in l:
            (key,val) = line.split()
            d[key] = val

    for key, value in d.items():
        print(key, ' : ', value)

#View
def view():
    list()
    input("To continue, press enter: \n")
    menu()

#Menu
def menu():
    print("Welcome to Contacts Book! Here are some things you can do!\n"
          "1. Add\n" #DONE
          "2. Delete\n" #DONE?!?
          "3. Edit\n"
          "4. Search\n" #DONE
          "5. View\n" #DONE
          "6. End\n") #DONE

    menu = 0
    while menu != 1:
        menu = input("Choose an option: ")
        if menu == "1":
            print("\n")
            add()
            break
        if menu == "2":
            print("\n")
            delete()
            break
        if menu == "3":
            print("\n")
            edit()
            break
        if menu == "4":
            print("\n")
            search()
            break
        if menu == "5":
            print("\n")
            view()
            break
        if menu == "6":
            print("\n")
            print('Shutting Down...')
            break
        else:
            print("Error you did not enter a correct value!")

#Start the process
menu()