import tkinter as tk
from tkinter import messagebox

class PhoneBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Phonebook")

        # Create a dictionary to store contacts
        self.contacts = {}

        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(pady=10)

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(pady=10)

        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(pady=10)

        # Add widgets to the first frame (for adding a contact)
        tk.Label(self.frame1, text="Name: ").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.frame1)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.frame1, text="Phone number: ").grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.frame1)
        self.phone_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.frame1, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=1, pady=5)

        # Widgets for displaying the contact list
        self.contact_listbox = tk.Listbox(self.frame2, width=50, height=10)
        self.contact_listbox.pack()

        # Widgets for deleting the selected contact
        self.delete_button = tk.Button(self.frame3, text="Delete Selected Contact", command=self.delete_contact)
        self.delete_button.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            self.contacts[name] = phone
            self.update_contact_list()
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Please enter both name and phone number!")

    def delete_contact(self):
        selected_contact = self.contact_listbox.curselection()
        if selected_contact:
            name = self.contact_listbox.get(selected_contact)
            del self.contacts[name.split(": ")[0]]
            self.update_contact_list()
        else:
            messagebox.showwarning("Error", "Please select a contact!")

    def update_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{name}: {phone}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBook(root)
    root.mainloop()
