import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def edit_contact(contacts):
    view_contacts(contacts)
    try:
        contact_index = int(input("Enter the number of the contact you want to edit: ")) - 1
        if 0 <= contact_index < len(contacts):
            contact = contacts[contact_index]
            print("Leave the field empty to keep the current value.")
            name = input(f"Enter new name ({contact['name']}): ") or contact['name']
            phone = input(f"Enter new phone number ({contact['phone']}): ") or contact['phone']
            email = input(f"Enter new email address ({contact['email']}): ") or contact['email']
            contacts[contact_index] = {"name": name, "phone": phone, "email": email}
            save_contacts(contacts)
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        contact_index = int(input("Enter the number of the contact you want to delete: ")) - 1
        if 0 <= contact_index < len(contacts):
            removed_contact = contacts.pop(contact_index)
            save_contacts(contacts)
            print(f"Contact {removed_contact['name']} deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()