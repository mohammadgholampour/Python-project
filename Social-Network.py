import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3


class SocialNetworkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Network")
        self.root.geometry("400x300")
        
        self.conn = sqlite3.connect('social_network.db')
        self.c = self.conn.cursor()
        self.create_tables()
        
        self.show_login_screen()
    
    def create_tables(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS users 
                          (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS posts 
                          (id INTEGER PRIMARY KEY, user_id INTEGER, content TEXT, 
                          FOREIGN KEY(user_id) REFERENCES users(id))''')
        self.conn.commit()

    
    def show_login_screen(self):
        self.clear_screen()
        
        self.lbl_title = tk.Label(self.root, text="Login to Social Network", font=("Arial", 16))
        self.lbl_title.pack(pady=20)

        self.lbl_username = tk.Label(self.root, text="Username:", font=("Arial", 12))
        self.lbl_username.pack()
        self.entry_username = tk.Entry(self.root, font=("Arial", 12))
        self.entry_username.pack(pady=5)

        self.lbl_password = tk.Label(self.root, text="Password:", font=("Arial", 12))
        self.lbl_password.pack()
        self.entry_password = tk.Entry(self.root, show="*", font=("Arial", 12))
        self.entry_password.pack(pady=5)

        self.btn_login = tk.Button(self.root, text="Login", command=self.login, font=("Arial", 12))
        self.btn_login.pack(pady=10)

        self.btn_register = tk.Button(self.root, text="Register", command=self.show_register_screen, font=("Arial", 12))
        self.btn_register.pack(pady=10)

    def show_register_screen(self):
        self.clear_screen()

        self.lbl_title = tk.Label(self.root, text="Register", font=("Arial", 16))
        self.lbl_title.pack(pady=20)

        self.lbl_username = tk.Label(self.root, text="Username:", font=("Arial", 12))
        self.lbl_username.pack()
        self.entry_username = tk.Entry(self.root, font=("Arial", 12))
        self.entry_username.pack(pady=5)

        self.lbl_password = tk.Label(self.root, text="Password:", font=("Arial", 12))
        self.lbl_password.pack()
        self.entry_password = tk.Entry(self.root, show="*", font=("Arial", 12))
        self.entry_password.pack(pady=5)

        self.btn_register = tk.Button(self.root, text="Register", command=self.register, font=("Arial", 12))
        self.btn_register.pack(pady=10)

        self.btn_back = tk.Button(self.root, text="Back to Login", command=self.show_login_screen, font=("Arial", 12))
        self.btn_back.pack(pady=10)

    # تابع ثبت‌نام
    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            self.c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            messagebox.showinfo("Success", "Registration successful")
            self.show_login_screen()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")

    # تابع ورود
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        self.c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.c.fetchone()
        if user:
            messagebox.showinfo("Success", "Login successful")
            self.user_id = user[0]
            self.show_post_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    # نمایش صفحه ارسال پست
    def show_post_screen(self):
        self.clear_screen()

        self.lbl_title = tk.Label(self.root, text="Post Something", font=("Arial", 16))
        self.lbl_title.pack(pady=20)

        self.txt_post = tk.Text(self.root, height=5, width=40, font=("Arial", 12))
        self.txt_post.pack(pady=10)

        self.btn_submit = tk.Button(self.root, text="Submit", command=self.submit_post, font=("Arial", 12))
        self.btn_submit.pack(pady=10)

        self.btn_view_posts = tk.Button(self.root, text="View All Posts", command=self.show_all_posts, font=("Arial", 12))
        self.btn_view_posts.pack(pady=5)

        self.btn_logout = tk.Button(self.root, text="Logout", command=self.show_login_screen, font=("Arial", 12))
        self.btn_logout.pack(pady=5)

    # تابع ارسال پست
    def submit_post(self):
        content = self.txt_post.get("1.0", tk.END).strip()
        if content:
            self.c.execute("INSERT INTO posts (user_id, content) VALUES (?, ?)", (self.user_id, content))
            self.conn.commit()
            messagebox.showinfo("Success", "Post submitted")
            self.txt_post.delete("1.0", tk.END)
        else:
            messagebox.showerror("Error", "Post content cannot be empty")

    # نمایش تمامی پست‌ها
    def show_all_posts(self):
        all_posts_window = tk.Toplevel(self.root)
        all_posts_window.title("All Posts")
        all_posts_window.geometry("400x400")

        posts_frame = tk.Frame(all_posts_window)
        posts_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(posts_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        posts_listbox = tk.Listbox(posts_frame, yscrollcommand=scrollbar.set, font=("Arial", 12))
        posts_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=posts_listbox.yview)

        self.c.execute("SELECT users.username, posts.content FROM posts JOIN users ON posts.user_id = users.id")
        posts = self.c.fetchall()

        for post in posts:
            posts_listbox.insert(tk.END, f"{post[0]}: {post[1]}")


    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    
    def on_close(self):
        self.conn.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = SocialNetworkApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()