import tkinter as tk
from tkinter import messagebox

current_balance = 1000

class ATM(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("ATM")
        self.geometry("800x600")
        self.configure(bg='#1a1a2e')
      
        self.title_font = ("Arial", 28, "bold")
        self.heading_font = ("Arial", 20, "bold")
        self.normal_font = ("Arial", 12)
        self.button_font = ("Arial", 11, "bold")

        self.colors = {
            'primary': '#16213e',
            'secondary': '#0f3460',
            'accent': '#e94560',
            'light': '#f1f1f1',
            'dark': '#1a1a2e',
            'success': '#4CAF50',
            'warning': '#FF9800',
            'card': '#667eea',
            'text_light': '#dddddd',
            'text_dark': '#333333'
        }
        
        # Container
        container = tk.Frame(self, bg=self.colors['dark'])
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        frames_list = [StartPage, MainMenu, WithdrawPage, DepositPage, BalancePage]
        for F in frames_list:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("StartPage")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=controller.colors['dark'])
        self.controller = controller
        
        # Header
        header = tk.Frame(self, bg=controller.colors['primary'], height=150)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        title = tk.Label(header, text="ATM", font=controller.title_font, 
                        bg=controller.colors['primary'], fg='white')
        title.pack(expand=True)
        
        subtitle = tk.Label(header, text="Secure Banking", font=controller.normal_font,
                          bg=controller.colors['primary'], fg=controller.colors['light'])
        subtitle.pack(pady=(0, 20))
        
        # Login Container
        login_frame = tk.Frame(self, bg=controller.colors['dark'])
        login_frame.pack(expand=True, fill='both', padx=50, pady=30)
        
        # Card simulation
        card_frame = tk.Frame(login_frame, bg='#2d3047', highlightthickness=2,
                             highlightbackground='#3d405b', relief='flat')
        card_frame.pack(pady=(0, 40), ipadx=20, ipady=20)
        
        tk.Label(card_frame, text="💳", font=("Arial", 24), bg='#2d3047', fg='white').pack(pady=(10, 5))
        tk.Label(card_frame, text="Enter Your PIN", font=controller.normal_font,
                bg='#2d3047', fg=controller.colors['light']).pack()
        
        # PIN Entry
        pin_frame = tk.Frame(self, bg=controller.colors['dark'])
        pin_frame.pack(pady=20)
        
        tk.Label(pin_frame, text="PIN Code:", font=controller.normal_font,
                bg=controller.colors['dark'], fg='white').pack(anchor='w')
        
        self.pin_var = tk.StringVar()
        pin_entry = tk.Entry(pin_frame, textvariable=self.pin_var, font=("Arial", 18),
                           show="•", width=20, bg='#2d3047', fg='white',
                           insertbackground='white', justify='center')
        pin_entry.pack(pady=10, ipady=10)
        pin_entry.focus_set()
        
        # Error label
        self.error_label = tk.Label(login_frame, text="", font=controller.normal_font,
                                   bg=controller.colors['dark'], fg=controller.colors['accent'])
        self.error_label.pack()
        
        # Login Button
        login_btn = tk.Button(login_frame, text="🔓 ACCESS ACCOUNT", 
                            font=controller.button_font,
                            bg=controller.colors['accent'], fg='white',
                            activebackground='#ff6b88', activeforeground='white',
                            padx=30, pady=12,
                            command=lambda: self.check_pin(controller))
        login_btn.pack(pady=20)
        
        # Footer
        footer = tk.Frame(self, bg=controller.colors['primary'], height=60)
        footer.pack(fill='x', side='bottom')
        footer.pack_propagate(False)
        
        tk.Label(footer, text="24/7 Banking Services • 100% Secure", 
                font=("Arial", 10), bg=controller.colors['primary'], fg='#aaaaaa').pack(expand=True)
    
    def check_pin(self, controller):
        pin = self.pin_var.get()
        if len(pin) == 4 and pin.isdigit() and 1000 <= int(pin) <= 9999:
            self.pin_var.set("")
            self.error_label.config(text="")
            controller.show_frame("MainMenu")
        else:
            self.error_label.config(text="⚠ Invalid PIN! Please enter a 4-digit number.")

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=controller.colors['dark'])
        self.controller = controller
        
        # Header
        header = tk.Frame(self, bg=controller.colors['primary'], height=120)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        welcome_label = tk.Label(header, text="Welcome Back!", font=controller.heading_font,
                                bg=controller.colors['primary'], fg='white')
        welcome_label.pack(expand=True, pady=20)
        
        # Services Grid
        services_frame = tk.Frame(self, bg=controller.colors['dark'])
        services_frame.pack(expand=True, fill='both', padx=30, pady=30)
        
        # Buttons Grid
        buttons = [
            ("💰 WITHDRAW", controller.colors['secondary'], lambda: controller.show_frame("WithdrawPage"), "💵"),
            ("💳 DEPOSIT", controller.colors['success'], lambda: controller.show_frame("DepositPage"), "📥"),
            ("📊 BALANCE", controller.colors['warning'], lambda: controller.show_frame("BalancePage"), "📈"),
            ("🚪 LOGOUT", controller.colors['accent'], lambda: controller.show_frame("StartPage"), "🔒")
        ]
        
        for i, (text, color, command, icon) in enumerate(buttons):
            btn_frame = tk.Frame(services_frame, bg=controller.colors['dark'])
            btn_frame.grid(row=i//2, column=i%2, padx=10, pady=10, sticky='nsew')
            
            services_frame.grid_columnconfigure(i%2, weight=1)
            services_frame.grid_rowconfigure(i//2, weight=1)
            
            btn = tk.Button(btn_frame, text=f"{icon}\n{text}", 
                          font=controller.button_font,
                          bg=color, fg='white',
                          activebackground=color,
                          padx=20, pady=30,
                          command=command, wraplength=150)
            btn.pack(fill='both', expand=True)
        
        # Footer
        footer = tk.Frame(self, bg='#2d3047', height=50)
        footer.pack(fill='x', side='bottom')
        tk.Label(footer, text=f"Current Balance: €{current_balance:.2f}", 
                font=("Arial", 10, 'bold'), bg='#2d3047', fg='white').pack(expand=True)

class WithdrawPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=controller.colors['dark'])
        self.controller = controller
        
        # Header with back button
        header = tk.Frame(self, bg=controller.colors['primary'], height=100)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        back_btn = tk.Button(header, text="← Back", font=controller.button_font,
                           bg=controller.colors['primary'], fg='white',
                           activebackground=controller.colors['primary'],
                           activeforeground='white',
                           command=lambda: controller.show_frame("MainMenu"))
        back_btn.pack(side='left', padx=20)
        
        tk.Label(header, text="Cash Withdrawal", font=controller.heading_font,
                bg=controller.colors['primary'], fg='white').pack(expand=True)
        
        # Quick Amounts
        quick_frame = tk.Frame(self, bg=controller.colors['dark'])
        quick_frame.pack(pady=30)
        
        tk.Label(quick_frame, text="Quick Withdraw", font=controller.normal_font,
                bg=controller.colors['dark'], fg='white').pack()
        
        amounts = [10, 20, 50, 100, 200, 500]
        buttons_frame = tk.Frame(quick_frame, bg=controller.colors['dark'])
        buttons_frame.pack(pady=20)
        
        for i, amount in enumerate(amounts):
            btn = tk.Button(buttons_frame, text=f"€{amount}",
                          font=controller.button_font,
                          bg=controller.colors['secondary'], fg='white',
                          activebackground='#2d4059',
                          command=lambda a=amount: self.withdraw(a, controller),
                          width=8, height=2)
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
        
        # Custom Amount
        custom_frame = tk.Frame(self, bg=controller.colors['dark'])
        custom_frame.pack(pady=30, padx=50)
        
        tk.Label(custom_frame, text="Custom Amount:", font=controller.normal_font,
                bg=controller.colors['dark'], fg='white').pack()
        
        self.custom_var = tk.StringVar()
        custom_entry = tk.Entry(custom_frame, textvariable=self.custom_var,
                              font=("Arial", 16), justify='center',
                              bg='#2d3047', fg='white',
                              insertbackground='white')
        custom_entry.pack(pady=10, ipady=8, ipadx=20)
        custom_entry.bind('<Return>', lambda e: self.withdraw_custom(controller))
        
        custom_btn = tk.Button(custom_frame, text="WITHDRAW CUSTOM AMOUNT",
                             font=controller.button_font,
                             bg=controller.colors['accent'], fg='white',
                             command=lambda: self.withdraw_custom(controller),
                             padx=20, pady=10)
        custom_btn.pack(pady=10)
        
        # Balance indicator
        balance_frame = tk.Frame(self, bg='#2d3047')
        balance_frame.pack(fill='x', side='bottom', pady=10)
        tk.Label(balance_frame, text=f"Available: €{current_balance:.2f}",
                font=("Arial", 12, 'bold'), bg='#2d3047', fg='white').pack(pady=10)
    
    def withdraw(self, amount, controller):
        global current_balance
        if amount > current_balance:
            messagebox.showwarning("Insufficient Funds",
                                 f"Your balance is €{current_balance:.2f}")
        else:
            current_balance -= amount
            messagebox.showinfo("Success",
                              f"€{amount:.2f} withdrawn successfully!\nNew Balance: €{current_balance:.2f}")
            controller.show_frame("MainMenu")
    
    def withdraw_custom(self, controller):
        try:
            amount = float(self.custom_var.get())
            self.withdraw(amount, controller)
            self.custom_var.set("")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

class DepositPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=controller.colors['dark'])
        self.controller = controller
        
        # Header
        header = tk.Frame(self, bg=controller.colors['primary'], height=100)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        back_btn = tk.Button(header, text="← Back", font=controller.button_font,
                           bg=controller.colors['primary'], fg='white',
                           activebackground=controller.colors['primary'],
                           activeforeground='white',
                           command=lambda: controller.show_frame("MainMenu"))
        back_btn.pack(side='left', padx=20)
        
        tk.Label(header, text="Cash Deposit", font=controller.heading_font,
                bg=controller.colors['primary'], fg='white').pack(expand=True)
        
        # Deposit interface
        deposit_frame = tk.Frame(self, bg=controller.colors['dark'])
        deposit_frame.pack(expand=True, padx=50, pady=50)
        
        # Deposit icon
        icon_frame = tk.Frame(deposit_frame, bg='#2d3047', width=120, height=120)
        icon_frame.pack_propagate(False)
        icon_frame.pack(pady=(0, 30))
        
        tk.Label(icon_frame, text="📥", font=("Arial", 48), bg='#2d3047', fg='white').pack(expand=True)
        
        tk.Label(deposit_frame, text="Enter Deposit Amount:", font=controller.normal_font,
                bg=controller.colors['dark'], fg='white').pack()
        
        self.amount_var = tk.StringVar()
        amount_entry = tk.Entry(deposit_frame, textvariable=self.amount_var,
                              font=("Arial", 18), justify='center',
                              bg='#2d3047', fg='white',
                              insertbackground='white', width=20)
        amount_entry.pack(pady=20, ipady=10)
        amount_entry.focus_set()
        
        # Buttons
        btn_frame = tk.Frame(deposit_frame, bg=controller.colors['dark'])
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="DEPOSIT", font=controller.button_font,
                 bg=controller.colors['success'], fg='white',
                 command=self.deposit,
                 padx=40, pady=25).pack(side='left', padx=20)
        
        tk.Button(btn_frame, text="CLEAR", font=controller.button_font,
                 bg=controller.colors['warning'], fg='white',
                 command=lambda: self.amount_var.set(""),
                 padx=40, pady=25).pack(side='left', padx=20)
    
    def deposit(self):
        global current_balance
        try:
            amount = float(self.amount_var.get())
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount")
                return
            
            current_balance += amount
            messagebox.showinfo("Success",
                              f"€{amount:.2f} deposited successfully!\nNew Balance: €{current_balance:.2f}")
            self.amount_var.set("")
            self.controller.show_frame("MainMenu")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")

class BalancePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=controller.colors['dark'])
        self.controller = controller
        
        # Header
        header = tk.Frame(self, bg=controller.colors['primary'], height=100)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        back_btn = tk.Button(header, text="← Back", font=controller.button_font,
                           bg=controller.colors['primary'], fg='white',
                           activebackground=controller.colors['primary'],
                           activeforeground='white',
                           command=lambda: controller.show_frame("MainMenu"))
        back_btn.pack(side='left', padx=20)
        
        tk.Label(header, text="Account Balance", font=controller.heading_font,
                bg=controller.colors['primary'], fg='white').pack(expand=True)
        
        # Balance Card
        main_frame = tk.Frame(self, bg=controller.colors['dark'])
        main_frame.pack(expand=True, fill='both', padx=30, pady=30)
        
        # Card-like display
        card = tk.Frame(main_frame, bg=controller.colors['card'], highlightthickness=0)
        card.pack(expand=True, fill='both', pady=20)
        
        # Account info
        info_frame = tk.Frame(card, bg=controller.colors['card'])
        info_frame.pack(expand=True)
        
        tk.Label(info_frame, text="ACCOUNT SUMMARY", font=("Arial", 14, 'bold'),
                bg=controller.colors['card'], fg=controller.colors['text_light']).pack(pady=(30, 10))
        
        # Balance display
        self.balance_label = tk.Label(info_frame, text=f"€{current_balance:.2f}",
                                     font=("Arial", 48, 'bold'),
                                     bg=controller.colors['card'], fg='white')
        self.balance_label.pack(pady=20)
        
        tk.Label(info_frame, text="Available Balance", font=controller.normal_font,
                bg=controller.colors['card'], fg=controller.colors['text_light']).pack()
        
        # Recent transactions (simulated)
        trans_frame = tk.Frame(main_frame, bg='#2d3047')
        trans_frame.pack(fill='x', pady=20)
        
        tk.Label(trans_frame, text="Recent Activity", font=controller.normal_font,
                bg='#2d3047', fg='white').pack(anchor='w', padx=20, pady=10)
        
        transactions = [
            ("ATM Withdrawal", "-€50.00", "Today"),
            ("Deposit", "+€200.00", "Yesterday"),
            ("ATM Withdrawal", "-€20.00", "2 days ago")
        ]
        
        for desc, amount, date in transactions:
            trans_item = tk.Frame(trans_frame, bg='#2d3047')
            trans_item.pack(fill='x', padx=20, pady=5)
            
            tk.Label(trans_item, text=desc, font=("Arial", 10),
                    bg='#2d3047', fg='#aaaaaa').pack(side='left')
            tk.Label(trans_item, text=amount, font=("Arial", 10, 'bold'),
                    bg='#2d3047', fg='white').pack(side='right')
            tk.Label(trans_item, text=date, font=("Arial", 9),
                    bg='#2d3047', fg='#777777').pack(side='right', padx=20)
        
        # Action buttons
        btn_frame = tk.Frame(main_frame, bg=controller.colors['dark'])
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="PRINT STATEMENT", font=controller.button_font,
                 bg=controller.colors['secondary'], fg='white',
                 padx=20, pady=10).pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="BACK TO MENU", font=controller.button_font,
                 bg=controller.colors['accent'], fg='white',
                 command=lambda: controller.show_frame("MainMenu"),
                 padx=20, pady=10).pack(side='left', padx=10)

if __name__ == "__main__":
    app = ATM()
    app.mainloop()