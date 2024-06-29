from tkinter import *
from tkinter import ttk
from functions import Application
def setwindow(root):
    """
    The function setwindow() creates the main user window
    """
    root.title("Activity tracker")
    root.resizable(True, True)
    w = 700
    h = 300

    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2 - 25)
    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))
root = Tk()
root.configure(background='white')
setwindow(root)

def add_new_application():
    def setwindow(root_add_func):
        root_add_func.title("New application")
        root_add_func.resizable(False, False)
        w = 405
        h = 200

        x = 0
        y = 0
        root_add_func.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))
    
    root_add_func = Tk()
    root_add_func.configure(background='white')
    setwindow(root_add_func)

    # Create labels and entry fields for add_new_application window
    company_name_label = Label(root_add_func, font="Georgia 13", text="Company name: ", bg="white")
    company_name_label.grid(row=0, column=0)
    company_name_entry = Entry(root_add_func, font="Georgia 13", width=20, background="white", bg="white")
    company_name_entry.grid(row=0, column=1)

    contact_date_label = Label(root_add_func, font="Georgia 13", text="Contact date: ", bg="white")  
    contact_date_label.grid(row=1, column=0)
    contact_date_entry = Entry(root_add_func, font="Georgia 13", width=20)
    contact_date_entry.grid(row=1, column=1)
    contact_date_hint_label = Label(root_add_func, font="Georgia 13", text="XXXX-XX-XX format", bg="white") 
    contact_date_hint_label.grid(row=1, column=2)

    action_label = Label(root_add_func, font="Georgia 13", text="Action: ", bg="white") 
    action_label.grid(row=2, column=0)
    action_entry = Entry(root_add_func, font="Georgia 13", width=20, bg='white')
    action_entry.grid(row=2, column=1)

    job_title_label = Label(root_add_func, font="Georgia 13", text="Job title: ", bg="white")
    job_title_label.grid(row=3, column=0)
    job_title_entry = Entry(root_add_func, font="Georgia 13", width=20)
    job_title_entry.grid(row=3, column=1)

    job_link_label = Label(root_add_func, font="Georgia 13", text="Job link: ", bg="white")
    job_link_label.grid(row=4, column=0)
    job_link_entry = Entry(root_add_func, font="Georgia 13", width=20)
    job_link_entry.grid(row=4, column=1)

    contact_name_label = Label(root_add_func, font="Georgia 13", text="Contact name: ", bg="white")
    contact_name_label.grid(row=5, column=0)
    contact_name_entry = Entry(root_add_func, font="Georgia 13", width=20)
    contact_name_entry.grid(row=5, column=1)


    def submit_addition():
        item = Application(company_name_entry.get(), 
                           contact_date_entry.get(), 
                           action_entry.get(),
                            job_title_entry.get(), 
                            job_link_entry.get(), 
                            contact_name_entry.get()
                            )
        item.add_new_application()
        root_add_func.destroy() # close the window "add new application"
    save_new_line_button = ttk.Button(root_add_func, text="Save New Line", command=submit_addition)
    save_new_line_button.grid(row=6, column=1)

def change_application():
    pass
i = 0
def show_application():
    def setwindow(root_show_all_func):
        root_show_all_func.title("Your applications")
        root_show_all_func.resizable(True, True)
        w = 500
        h = 600

        x = 0
        y = 0
        root_show_all_func.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))
    
    def display_tables():
        global i
        i = 0
        
        app_instance = Application("", "", "", "", "", "")
        tables = app_instance.select_all()

        for table in tables:
            company_label = Label(root_show_all_func, font="Georgia 13", text=table[1], bg="white")
            company_label.grid(row=i, column=0)
            contact_date_label = Label(root_show_all_func, font="Georgia 13", text=table[2], bg="white")
            contact_date_label.grid(row=i, column=1)
            action_label = Label(root_show_all_func, font="Georgia 13", text=table[3], bg="white")
            action_label.grid(row=i, column=2)
            job_title_label = Label(root_show_all_func, font="Georgia 13", text=table[4], bg="white")
            job_title_label.grid(row=i, column=3)
            job_link_label = Label(root_show_all_func, font="Georgia 13", text=table[5], bg="white")
            job_link_label.grid(row=i, column=4)
            contact_name_label = Label(root_show_all_func, font="Georgia 13", text=table[6], bg="white")
            contact_name_label.grid(row=i, column=5)
            
            # Define a function to handle the delete operation
            def create_delete_command(application_id):
                def delete_command():
                    delete_application(application_id)
                return delete_command

            delete_button = Button(root_show_all_func, text="Delete", command=create_delete_command(table[0]))
            delete_button.grid(row=i, column=6)
            i += 1

        # Place the fetch button under the last label
        fetch_button.grid(row=i, column=0, columnspan=7, pady=10)
               
    def delete_application(application_id):
        app_instance = Application("", "", "", "", "", "")
        app_instance.delete_application_by_id(application_id)
        display_tables()  # Refresh the table after deletion
    
    root_show_all_func = Tk()
    root_show_all_func.configure(background='white')
    setwindow(root_show_all_func)

    fetch_button = ttk.Button(root_show_all_func, text="Fetch Tables", command=display_tables)
    fetch_button.grid(row=0)  # Initial position, will be moved by display_tables()


label = Label(root, text="Menu", font=('Georgia 13'), bg="white")
label.place(anchor="n", x=350, y=50)

ttk.Button(root, text="Add new application", command=add_new_application).place(anchor="n", x=150, y=100)
ttk.Button(root, text="Change application", command=change_application).place(anchor="n", x=350, y=100)
ttk.Button(root, text="Show all application", command=show_application).place(anchor="n", x=550, y=100)

root.mainloop()