import tkinter as tk
from tkinter import messagebox


def save_password(site, username, password):
    with open("passwords.txt", "a") as f:
        f.write(f"{site} | {username} | {password}\n")


def load_passwords():
    try:
        with open("passwords.txt", "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def delete_password(site_to_delete):
    lines = load_passwords()
    with open("passwords.txt", "w") as f:
        for line in lines:
            if not line.startswith(site_to_delete):
                f.write(line)


def add_entry():
    site = site_entry.get()
    user = user_entry.get()
    pwd  = pass_entry.get()

    if site and user and pwd:
        save_password(site, user, pwd)
        messagebox.showinfo("Saved!", f"Password for '{site}' has been saved.")
        site_entry.delete(0, tk.END)
        user_entry.delete(0, tk.END)
        pass_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Fields", "Please fill in all three fields.")


def show_passwords():
    output.delete(1.0, tk.END)
    entries = load_passwords()

    if entries:
        output.insert(tk.END, "Website          | Username        | Password\n")
        output.insert(tk.END, "-" * 55 + "\n")
        for entry in entries:
            output.insert(tk.END, entry)
    else:
        output.insert(tk.END, "No passwords saved yet.\nAdd one using the fields above!")


def delete_entry():
    site = site_entry.get()

    if site:
        delete_password(site)
        messagebox.showinfo("Deleted", f"All entries for '{site}' have been removed.")
        show_passwords()
    else:
        messagebox.showwarning("No Input", "Please enter a website name in the Website field to delete.")


def clear_fields():
    site_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    output.delete(1.0, tk.END)


window = tk.Tk()
window.title("🔒 Password Manager")
window.geometry("560x460")
window.resizable(False, False)

tk.Label(
    window,
    text="Password Manager",
    font=("Arial", 18, "bold")
).grid(row=0, column=0, columnspan=3, pady=(15, 5))

tk.Label(
    window,
    text="Store your passwords safely on this computer",
    font=("Arial", 10),
    fg="gray"
).grid(row=1, column=0, columnspan=3, pady=(0, 15))

tk.Label(window, text="Website:", font=("Arial", 11)).grid(
    row=2, column=0, padx=15, pady=6, sticky="e")
site_entry = tk.Entry(window, width=32, font=("Arial", 11))
site_entry.grid(row=2, column=1, columnspan=2, padx=10, sticky="w")

tk.Label(window, text="Username:", font=("Arial", 11)).grid(
    row=3, column=0, padx=15, pady=6, sticky="e")
user_entry = tk.Entry(window, width=32, font=("Arial", 11))
user_entry.grid(row=3, column=1, columnspan=2, padx=10, sticky="w")

tk.Label(window, text="Password:", font=("Arial", 11)).grid(
    row=4, column=0, padx=15, pady=6, sticky="e")
pass_entry = tk.Entry(window, width=32, font=("Arial", 11), show="*")
pass_entry.grid(row=4, column=1, columnspan=2, padx=10, sticky="w")

btn_frame = tk.Frame(window)
btn_frame.grid(row=5, column=0, columnspan=3, pady=14)

tk.Button(
    btn_frame, text="💾  Save Password", width=16, font=("Arial", 10),
    bg="#4CAF50", fg="white", command=add_entry
).grid(row=0, column=0, padx=6)

tk.Button(
    btn_frame, text="👁  View All", width=14, font=("Arial", 10),
    bg="#2196F3", fg="white", command=show_passwords
).grid(row=0, column=1, padx=6)

tk.Button(
    btn_frame, text="🗑  Delete", width=12, font=("Arial", 10),
    bg="#f44336", fg="white", command=delete_entry
).grid(row=0, column=2, padx=6)

tk.Button(
    btn_frame, text="✖  Clear", width=10, font=("Arial", 10),
    command=clear_fields
).grid(row=0, column=3, padx=6)

tk.Label(window, text="Saved Passwords:", font=("Arial", 11, "bold")).grid(
    row=6, column=0, columnspan=3, padx=15, sticky="w")

output = tk.Text(window, height=11, width=62, font=("Courier", 10), state="normal")
output.grid(row=7, column=0, columnspan=3, padx=15, pady=(4, 15))

output.insert(tk.END, "Welcome! Enter a website, username, and password above,\nthen click 'Save Password' to get started.\n\nClick 'View All' to see saved passwords.")

window.mainloop()