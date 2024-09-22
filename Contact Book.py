contacts = []
def main_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Thank you for using the Contact Book. Have a Nice Day!")
            break
        else:
            print("Invalid choice. Please try again.")
def add_contact():
    name = input("Enter name: ")
    phone = int(input("Enter phone number: "))
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        "Name": name,
        "Phone": phone,
        "E-mail": email,
        "Address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['Name']} - {contact['Phone']}")
def search_contact():
    search_term = input("Enter Name or Phone Number to search: ")
    results = []
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in str(contact['Phone']):
            results.append(contact)
    if results:
        print("\n--- Search Results ---")
        for i, contact in enumerate(results, 1):
            print(f"{i}. {contact['Name']} - {contact['Phone']}")
    else:
        print("No matching contacts found.")
def update_contact():
    view_contacts()
    if not contacts:
        return
    index = int(input("Enter the number of the contact to update: ")) - 1
    
    if 0 <= index < len(contacts):
        contact = contacts[index]
        print(f"\nUpdating contact: {contact['Name']}")
        contact['Name'] = input("Enter new name (or press Enter to keep current): ") or contact['Name']
        contact['Phone'] = (input("Enter new phone (or press Enter to keep current): ")) or (contact['Phone'])
        contact['E-mmail'] = input("Enter new email (or press Enter to keep current): ") or contact['E-mail']
        contact['Address'] = input("Enter new address (or press Enter to keep current): ") or contact['Address']
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")
def delete_contact():
    view_contacts()
    if not contacts:
        return
    index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"Contact '{deleted_contact['Name']}' deleted successfully!")
    else:
        print("Invalid contact number.")
main_menu()