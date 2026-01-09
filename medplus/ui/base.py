import tkinter as tk
from tkinter import ttk

class MedPlusApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MedPlus Hospital Management System")
        self.geometry("1000x800")
        
        # Style Configuration
        self.style = ttk.Style(self)
        self.style.theme_use('clam')  # 'clam' is usually a good base for custom styling
        
        # Colors
        self.primary_color = "#008080" # Teal
        self.secondary_color = "#ADD8E6" # Light Blue (from original)
        self.bg_color = "#f0f0f0"
        
        self.configure(bg=self.bg_color)
        
        # Configure Styles
        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('TLabel', background=self.bg_color, font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6)
        self.style.map('TButton', background=[('active', self.primary_color)])

        self.style.configure('Header.TLabel', font=('Helvetica', 24, 'bold'), foreground=self.primary_color)
        self.style.configure('SubHeader.TLabel', font=('Helvetica', 14, 'bold'), foreground="#333")
        
        self.current_frame = None

    def switch_frame(self, frame_class, *args, **kwargs):
        """Destroys current frame and replaces it with a new one."""
        if self.current_frame:
            self.current_frame.destroy()
        
        self.current_frame = frame_class(self, *args, **kwargs)
        self.current_frame.pack(fill="both", expand=True)

class BaseFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
