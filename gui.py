import customtkinter as ctk


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x480")


        self.login_frame = ctk.CTkFrame(root)
        self.login_frame.pack(pady=20, padx=15, fill="both", expand=True)

        self.username_entry = ctk.CTkEntry(master=self.login_frame, placeholder_text="Username")
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = ctk.CTkEntry(master=self.login_frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=12, padx=10)

        self.login_button = ctk.CTkButton(master=self.login_frame, text="Login", corner_radius=32,
                                            fg_color="transparent", hover_color="#8A2BE2", border_color="#F0FFFF",
                                          border_width=2, command=self.login)
        self.login_button.pack(pady=12, padx=10)

    def login(self):
        if self.username_entry.get() == "admin" and self.password_entry.get() == "password":
            self.login_frame.pack_forget()
            MainApplicationWindow(self.root)
        else:
            self.incorrect_user_credentials()

    def incorrect_user_credentials(self):
        error_window = ctk.CTkToplevel(self.root)
        error_window.geometry("300x150")

        #Clear previous attempts
        self.username_entry.delete(0,"end")
        self.password_entry.delete(0,"end")

        incorrect_credentials_label = ctk.CTkLabel(error_window, text="Incorrect username or password!")
        incorrect_credentials_label.pack(pady=20, padx=10)

        clickOK_button = ctk.CTkButton(error_window, text="OK", command=error_window.destroy)
        clickOK_button.pack(pady=12, padx=10)


class MainApplicationWindow:
    def __init__(self, root):
        self.root = root

        self.main_frame = ctk.CTkFrame(master=root, fg_color="#34568B", border_color="#000000",
                                       border_width=2)
        self.main_frame.pack(fill="both", expand=True)


        self.main_label = ctk.CTkLabel(master=self.main_frame, text="Welcome to the Various Calculators application!",
                                       font=("Roboto", 20),text_color="#FFFFFF")
        self.main_label.pack(pady=10, padx=10)

        self.tabview_frame = ctk.CTkFrame(master=self.main_frame, corner_radius=10)
        self.tabview_frame.pack(pady=(root.winfo_height()//4, 0), padx=(root.winfo_width()//8, root.winfo_width()//8),fill="both", expand=True)

        self.tabview = ctk.CTkTabview(master=self.tabview_frame)
        self.tabview.pack(pady=30,padx=20, fill="both", expand=True)

        self.tabview.add("Algebra")
        self.tabview.add("Trigonometry")

        self.add_buttons_to_algebra_tab(self.tabview.tab("Algebra"))
        #Buttons for Algebraic Formulas
        #Remember to add commands for each button
        self.algebra_quadratic_formula_button = ctk.CTkButton(master=self.tabview.tab("Algebra"), text="Quadratic Formula",
                                                              corner_radius=32, fg_color="#F7CAC9", border_color="#FFFFFF",
                                                              width=200, height=50)

        self.algebra_distance_formula_button = ctk.CTkButton(master=self.tabview.tab("Algebra"), text="Distance Formula",
                                                             corner_radius=32, fg_color="#88B04B", border_color="#FFFFFF",
                                                             width=200, height=50)

        self.algebra_midpoint_formula_button = ctk.CTkButton(master=self.tabview.tab("Algebra"), text="Midpoint Formula",
                                                            corner_radius=32, fg_color="#FF6F61", border_color="#F0FFFF",
                                                             width=200, height=50)



        self.trigonometry_label = ctk.CTkLabel(master=self.tabview.tab("Trigonometry"), text="Trigonometry")
        self.trigonometry_label.pack(pady=20, padx=20)

    def add_buttons_to_algebra_tab(self, algebra_tab):
        num_columns = 2
        buttons = [
                ("Quadratic Formula", "#F7CAC9"),
                ("Distance Formula", "#88B04B"),
                ("Midpoint Formula", "#FF6F61")
            ]

        for i, (text, color) in enumerate(buttons):
            button = ctk.CTkButton(master=algebra_tab, text=text, corner_radius=10, fg_color=color, width=180, height=50)

            row = i //num_columns
            col = i % num_columns
            button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        for col in range(num_columns):
            algebra_tab.grid_columnconfigure(col, weight=1)

        num_rows = (len(buttons) + num_columns -1) //num_columns
        for row in range(num_rows):
            algebra_tab.grid_rowconfigure(row, weight=1)




root = ctk.CTk()

login_window = LoginWindow(root)

root.mainloop()
