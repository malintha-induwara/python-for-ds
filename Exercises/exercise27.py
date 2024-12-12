#simple contact managment system

#create a program that store and manage contacts in a file name contacts.txt
# each contact entry should have name,phone number and email address

## Feature to implement
# 1. view all contacts (read and display all contacts from the file)
# 2. Add a contact (append a new contact to the file)
# 3. exit

#Structure of the file
# name,phone number,email address


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    
    with open("contacts.txt","a") as file:
        new_contact = name + "," + phone + "," + email + "\n"
        file.write(new_contact)


def view_contacts():
    with open("contacts.txt","r") as file:
        content = file.readlines()
        for line in content:
            print(line)

while True:
    print("1. View all contacts")
    print("2. Add a contact")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        view_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        print("Exiting from the program")
        break
    else:
        print("Invalid choice")


