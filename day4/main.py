import contact
import contact_manager as cm
import re
def get_name()->str:
    while True:
        name=input("Enter the name of the contact: ")
        if not name:
            print("Invalid Input")
        else:
            return name

def get_phn_no()->str:
    while True:
        n=input("Enter the phone number of the contact: ")
        if n.isdigit() and len(n)==10:
            return n
        else:
            print("Invalid Input")

def get_email()->str:
    while True:
        a=input("Enter the email id of the contact: ")
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(pattern,a):
            return a
        else:
            print("Invalid Input")

def create_obj()->contact.Contact:
    return contact.Contact(get_name(),get_phn_no(),get_email())

def main():
    try:
        yo=cm.ContactManager()
    except ValueError as e:
        print(e)
        return
    while True:
        print("-----------------------Contact Manager-----------------------")
        print("1.Add a new Contact\n2.Search for a contact\n3.Update an existing contact\n4.Delete a contact\n5.Display all contacts\n6.Exit")
        try:
            a=int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Input!")
            continue
        match a:
            case 1:
                try:
                    yo.add_contact(create_obj())
                except ValueError as e:
                    print(e)
            case 2:
                if yo.search_contact_name(get_name()):
                    print("The contact exists!")
                else:
                    print("The contact doesnt exist")
            case 3:
                try:
                    yo.update_contact(get_name(),get_name(),get_phn_no(),get_email())
                    print("Contact updated")
                except ValueError as e:
                    print(e)
            case 4:
                try:
                    yo.delete_contact(get_name())
                    print("Contact Deleted!")
                except ValueError as e:
                    print(e)
            case 5:
                display_list=yo.display_contacts()
                if display_list:
                    for string in display_list:
                        print(string)
                else:
                    print("The contact list is empty")
            case 6:
                print("Exiting Program")
                try:
                    yo.save_contacts()
                except ValueError as e:
                    print(e)
                return
            case _:
                print("Invalid Input")


if __name__=="__main__":
    main()