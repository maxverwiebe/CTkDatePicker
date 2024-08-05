import customtkinter as ctk
from CTkDatePicker import *

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("450x200")
    root.title("CTkDatePicker Example")

    date_picker = CTkDatePicker(root)
    date_picker.pack(padx=20, pady=20)
    date_picker.set_allow_manual_input(False)
    
    # get value
    # date.picker.get_date()

    root.mainloop()
