import tkinter as tk
from tkinter import messagebox

current_balance = 1000


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Balanci': tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (F_fillestare, Menu, F_terheqjeve, F_depozitave, F_bilancit):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("F_fillestare")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class F_fillestare(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#83838B')
        self.controller = controller
        self.controller.title('ATM')
        self.controller.state('zoomed')

        heading_label = tk.Label(self, text='ATM', font=('orbitron', 45, 'bold'), background='#83838B')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#83838B')
        space_label.pack()

        password_label = tk.Label(self, text='Ju lutem, shtypni PIN-in tuaj:', font=('orbitron', 13), bg='#83838B')
        password_label.pack(pady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_password, font=('orbitron', 12), width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)

        def handle_focus_in(_):
            password_entry_box.configure(font=('orbitron', 12), show='*')

        password_entry_box.bind('<FocusIn>', handle_focus_in)

        def check_password():
            if int(my_password.get()) >= 1000 and int(my_password.get())<=9999:
                my_password.set('')
                incorrect_password_label['text'] = ''
                controller.show_frame('Menu')
            else:
               incorrect_password_label['text'] = 'Pin-i juaj eshte shenuar gabim! Ju lutem shenoni perseri!'
               
        enter_button = tk.Button(self, text='Enter', command=check_password, relief='groove', borderwidth=3, width=40,height=3)
        enter_button.pack(pady=10)

        incorrect_password_label = tk.Label(self, text='', font=('orbitron', 13), bg='#3d3d5c', anchor='n')
        incorrect_password_label.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#83838B')
        self.controller = controller

        heading_label = tk.Label(self, text='ATM', font=('orbitron', 45, 'bold'), background='#83838B')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self, text='Menu', font=('orbitron', 13), bg='#83838B')
        main_menu_label.pack()

        selection_label = tk.Label(self, text='Ju lutem zgjedhni sherbimin e kerkuar:', font=('orbitron', 13),
                                   bg='#83838B', anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='#3d3d5c')
        button_frame.pack(fill='both', expand=True)

        def terheqje():
            controller.show_frame('F_terheqjeve')

        withdraw_button = tk.Button(button_frame, text='Terheqje parash', command=terheqje, relief='raised',
                                    borderwidth=3, width=50, height=5)
        withdraw_button.grid(row=0, column=0, pady=5)

        def depozita():
            controller.show_frame('F_depozitave')

        deposit_button = tk.Button(button_frame, text='Deponim parash', command=depozita, relief='raised',
                                   borderwidth=3, width=50, height=5)
        deposit_button.grid(row=1, column=0, pady=5)

        def bilanci():
            controller.show_frame('F_bilancit')

        balance_button = tk.Button(button_frame, text='Gjendja e llogarise', command=bilanci, relief='raised',
                                   borderwidth=3, width=50, height=5)
        balance_button.grid(row=2, column=0, pady=5)

        def exit():
            controller.show_frame('F_fillestare')

        exit_button = tk.Button(button_frame, text='Exit', command=exit, relief='raised', borderwidth=3, width=50,
                                height=5)
        exit_button.grid(row=3, column=0, pady=5)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


class F_terheqjeve(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self, text='ATM', font=('orbitron', 45, 'bold'), background='#3d3d5c')
        heading_label.pack(pady=25)

        choose_amount_label = tk.Label(self, text='Qfare shume deshironi te terhiqni?', font=('orbitron', 13),
                                       bg='#3d3d5c')
        choose_amount_label.pack()

        button_frame = tk.Frame(self, bg='#83838B')
        button_frame.pack(fill='both', expand=True)

        def terheqje(amount):

            global current_balance

            if amount > current_balance:
                messagebox.showwarning('Paralajmrim!', 'Fonde jo të mjaftueshme!')
            else:
                current_balance -= amount
                controller.shared_data['Balanci'].set(current_balance)
                controller.show_frame('Menu')

        njezet_button = tk.Button(button_frame, text='10 euro', command=lambda: terheqje(10), relief='raised',borderwidth=3, width=50, height=5)
        njezet_button.grid(row=0, column=0, pady=5)

        dyzete_button = tk.Button(button_frame, text='20 euro', command=lambda: terheqje(20), relief='raised',borderwidth=3, width=50, height=5)
        dyzete_button.grid(row=1, column=0, pady=5)

        gjashtedhjete_button = tk.Button(button_frame, text='50 euro', command=lambda: terheqje(50), relief='raised', borderwidth=3, width=50, height=5)
        gjashtedhjete_button.grid(row=2, column=0, pady=5)

        njeqindshe_button = tk.Button(button_frame, text='100 euro', command=lambda: terheqje(100), relief='raised', borderwidth=3, width=50, height=5)
        njeqindshe_button.grid(row=0, column=1, pady=5, padx=555)

        dyqindshe_button = tk.Button(button_frame, text='200 euro', command=lambda: terheqje(200), relief='raised',borderwidth=3, width=50, height=5)
        dyqindshe_button.grid(row=1, column=1, pady=5)

        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame, textvariable=cash, width=59, justify='right')
        other_amount_entry.grid(row=2, column=1, pady=5, ipady=30)

        def other_amount(_):
            global current_balance

            if int(cash.get()) > current_balance:
               messagebox.showwarning('Paralajmrim!', 'Fonde jo të mjaftueshme!')
            else:
               current_balance -= int(cash.get())
               controller.shared_data['Balanci'].set(current_balance)
               cash.set('')
               controller.show_frame('Menu')

        other_amount_entry.bind('<Return>', other_amount)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

class F_depozitave(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self, text='ATM', font=('orbitron', 45, 'bold'), background='#3d3d5c')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#3d3d5c')
        space_label.pack()

        enter_amount_label = tk.Label(self, text='Shuma e deponuar', font=('orbitron', 13), bg='#3d3d5c')
        enter_amount_label.pack(pady=10)

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self, textvariable=cash, font=('orbitron', 12), width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            current_balance += int(cash.get())
            controller.shared_data['Balanci'].set(current_balance)
            controller.show_frame('Menu')
            cash.set('')

        enter_button = tk.Button(self, text='Enter', command=deposit_cash, relief='raised', borderwidth=3, width=40,
                                 height=3)
        enter_button.pack(pady=10)

        two_tone_label = tk.Label(self, bg='#83838B')
        two_tone_label.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


class F_bilancit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#33334d')
        self.controller = controller

        heading_label = tk.Label(self, text='ATM', font=('orbitron', 45, 'bold'), background='#33334d')
        heading_label.pack(pady=25)

        global current_balance
        controller.shared_data['Balanci'].set(current_balance)
        balance_label = tk.Label(self, textvariable=controller.shared_data['Balanci'], font=('orbitron', 13),
                                 bg='#33334d', anchor='w')
        balance_label.pack(fill='x')
        button_frame = tk.Frame(self, bg='#83838B')
        button_frame.pack(fill='both', expand=True)

        def menu():
            controller.show_frame('Menu')

        menu_button = tk.Button(button_frame, command=menu, text='Menu', relief='raised', borderwidth=3, width=50,
                                height=5)
        menu_button.grid(row=0, column=0, pady=5)

        def exit():
            controller.show_frame('F_fillestare')

        exit_button = tk.Button(button_frame, text='Exit', command=exit, relief='raised', borderwidth=3, width=50,
                                height=5)
        exit_button.grid(row=1, column=0, pady=5)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
