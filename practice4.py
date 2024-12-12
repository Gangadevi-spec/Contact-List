def add_contact(contacts, name, phone, email, address):
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact(contacts, search_term):
    results = [contact for contact in contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

def update_contact(contacts, name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("\nUpdating contact:")
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            contact['name'] = input("Enter new name (leave blank to keep unchanged): ") or contact['name']
            contact['phone'] = input("Enter new phone (leave blank to keep unchanged): ") or contact['phone']
            contact['email'] = input("Enter new email (leave blank to keep unchanged): ") or contact['email']
            contact['address'] = input("Enter new address (leave blank to keep unchanged): ") or contact['address']
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact(contacts, name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    contacts = []

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(contacts, name, phone, email, address)

        elif choice == '2':
            view_contacts(contacts)

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            search_contact(contacts, search_term)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            update_contact(contacts, name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)

        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
