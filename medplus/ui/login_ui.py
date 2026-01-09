import tkinter as tk
from tkinter import ttk, messagebox
from medplus.ui.base import BaseFrame
from medplus.auth import auth

class LoginFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # Center container
        container = ttk.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        ttk.Label(container, text="Login to MedPlus", style='Header.TLabel').pack(pady=20)
        
        # Username
        ttk.Label(container, text="Username").pack(anchor="w")
        self.username_var = tk.StringVar()
        ttk.Entry(container, textvariable=self.username_var, width=30).pack(pady=(0, 10))
        
        # Password
        ttk.Label(container, text="Password").pack(anchor="w")
        self.password_var = tk.StringVar()
        ttk.Entry(container, textvariable=self.password_var, show="*", width=30).pack(pady=(0, 10))
        
        # Role Selection (Optional but good for clarity based on original logic)
        ttk.Label(container, text="Role").pack(anchor="w")
        self.role_var = tk.StringVar(value="USER")
        role_frame = ttk.Frame(container)
        role_frame.pack(pady=(0, 20), fill="x")
        ttk.Radiobutton(role_frame, text="User", variable=self.role_var, value="USER").pack(side="left", padx=10)
        ttk.Radiobutton(role_frame, text="Admin", variable=self.role_var, value="ADMIN").pack(side="left", padx=10)
        
        # Buttons
        ttk.Button(container, text="Login", command=self.login).pack(fill="x", pady=5)
        ttk.Button(container, text="Create Account", command=self.go_to_register).pack(fill="x", pady=5)

    def login(self):
        username = self.username_var.get()
        password = self.password_var.get()
        role = self.role_var.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return

        success, message = auth.login(username, password, role)
        if success:
            # Import here to avoid circular dependency if possible, or organize imports better.
            # For now, I will assume Dashboard frames are passed or imported.
            # I'll rely on a method in master (MedPlusApp) to handle navigation after login.
            if hasattr(self.master, 'on_login_success'):
                self.master.on_login_success(role, username)
            else:
                messagebox.showinfo("Success", f"Logged in as {role}")
        else:
            messagebox.showerror("Error", message)

    def go_to_register(self):
        self.master.switch_frame(RegisterFrame)


class RegisterFrame(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        
        container = ttk.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        ttk.Label(container, text="Create Account", style='Header.TLabel').pack(pady=20)
        
        # Username
        ttk.Label(container, text="Username").pack(anchor="w")
        self.username_var = tk.StringVar()
        ttk.Entry(container, textvariable=self.username_var, width=30).pack(pady=(0, 10))
        
        # Password
        ttk.Label(container, text="Password").pack(anchor="w")
        self.password_var = tk.StringVar()
        ttk.Entry(container, textvariable=self.password_var, show="*", width=30).pack(pady=(0, 10))
        
        # Role
        ttk.Label(container, text="Role").pack(anchor="w")
        self.role_var = tk.StringVar(value="USER")
        role_frame = ttk.Frame(container)
        role_frame.pack(pady=(0, 20), fill="x")
        ttk.Radiobutton(role_frame, text="User", variable=self.role_var, value="USER").pack(side="left", padx=10)
        ttk.Radiobutton(role_frame, text="Admin", variable=self.role_var, value="ADMIN").pack(side="left", padx=10)
        
        # Buttons
        ttk.Button(container, text="Register", command=self.register).pack(fill="x", pady=5)
        ttk.Button(container, text="Back to Login", command=self.go_to_login).pack(fill="x", pady=5)

    def register(self):
        username = self.username_var.get()
        password = self.password_var.get()
        role = self.role_var.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return

        success, message = auth.register(username, password, role)
        if success:
            messagebox.showinfo("Success", "Account created! Please login.")
            self.go_to_login()
        else:
            messagebox.showerror("Error", message)

    def go_to_login(self):
        self.master.switch_frame(LoginFrame)
