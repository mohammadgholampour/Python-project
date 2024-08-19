import tkinter as tk
from tkinter import messagebox
import random
import string

# تابع تولید و ذخیره‌سازی رمز عبور
def generate_password():
    length = int(entry_length.get())
    include_uppercase = var_uppercase.get()
    include_digits = var_digits.get()
    include_symbols = var_symbols.get()
    title = entry_title.get()

    if not title:
        messagebox.showwarning("Input Error", "Please enter a title for the password.")
        return

    # ایجاد مجموعه کاراکترها بر اساس انتخاب‌های کاربر
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # تولید رمز عبور
    password = ''.join(random.choice(characters) for _ in range(length))

    # نمایش رمز عبور
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

    # ذخیره‌سازی عنوان و رمز عبور در فایل
    with open("passwords.txt", "a") as file:
        file.write(f"{title}: {password}\n")

    # افزودن عنوان و رمز عبور به لیست‌نمایش
    listbox_passwords.insert(tk.END, f"{title}: {password}")

# تابع بارگذاری رمزهای عبور از فایل
def load_passwords():
    try:
        with open("passwords.txt", "r") as file:
            passwords = file.readlines()
            for password in passwords:
                listbox_passwords.insert(tk.END, password.strip())
    except FileNotFoundError:
        pass

# ایجاد پنجره اصلی
window = tk.Tk()
window.title("Password Generator")

# افزودن ویجت‌ها به پنجره
label_title = tk.Label(window, text="Title:")
label_title.pack()

entry_title = tk.Entry(window)
entry_title.pack()

label_length = tk.Label(window, text="Password Length:")
label_length.pack()

entry_length = tk.Entry(window)
entry_length.pack()

var_uppercase = tk.BooleanVar()
check_uppercase = tk.Checkbutton(window, text="Include Uppercase Letters", variable=var_uppercase)
check_uppercase.pack()

var_digits = tk.BooleanVar()
check_digits = tk.Checkbutton(window, text="Include Digits", variable=var_digits)
check_digits.pack()

var_symbols = tk.BooleanVar()
check_symbols = tk.Checkbutton(window, text="Include Symbols", variable=var_symbols)
check_symbols.pack()

button_generate = tk.Button(window, text="Generate Password", command=generate_password)
button_generate.pack()

entry_password = tk.Entry(window, width=30)
entry_password.pack()

label_saved = tk.Label(window, text="Saved Passwords:")
label_saved.pack()

listbox_passwords = tk.Listbox(window, width=50)
listbox_passwords.pack()

# بارگذاری رمزهای عبور ذخیره‌شده
load_passwords()

# اجرای حلقه اصلی برنامه
window.mainloop()