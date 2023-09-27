'''
Building my first Python Project in persuance to land a Job.
Jai Shri Ram
'''

import tkinter as tk
from tkinter import ttk
import shelve

def submitRecord():
    name = entry_name.get()
    age = entry_age.get()
    phone = entry_phone.get()
    address = entry_address.get()

    clearLabel()
    db = shelve.open('phoneBook')
    
    if not(recordCheck(db, name)):     # Update only if 'name' not in 'db'
        if age and phone and address:
            obj = {'Name': name, 'Age': age, 'Phone': phone, 'Address': address} 
            db[name] = obj
        else:
            display.set('Enter complete information')
    else:
        display.set('Name already present in Database')
    record_number.set('Number of Records present: '+ str(len(db)))
    clearLabel()
    db.close()

def retrieveRecord():
    db = shelve.open('phoneBook')
    name = entry_name.get()
    try:
        record = '\n'.join([f"{label}: {entry}" for label,entry in db[name].items()])
        display.set('')          # To clear Previous record
        display.set(record)
            
        for label,entry in db[name].items():    
            print(label,':', entry)
    except KeyError:
        print('No record found')
        clearLabel()
        display.set('No Record found!!')
    print()
    clearLabel()
    db.close()

def update():
    db = shelve.open('phoneBook')
    
    name = entry_name.get()
    age = entry_age.get()
    phone = entry_phone.get()
    address = entry_address.get()

    if recordCheck(db, name):
        obj = {'Name': name, 'Age': age, 'Phone': phone, 'Address': address} 
        db[name] = obj
    else:
        print('Name not present in Database')
        display.set('Name not present in Database')
    clearLabel()
    db.close()

def deleteRecord():
    '''
    Deletes a record based on Name provided
    '''
    db = shelve.open('phoneBook')
    name = entry_name.get()
    if recordCheck(db, name):
        del db[name]
        display.set('Record deleted Successfully!')
        record_number.set('Number of Records present: '+ str(len(db)))
    
    clearLabel()
        
            
def recordCheck(db, name):
    '''
    Checks if 'name' is present in 'db'
    '''
    if name in db.keys():
        return True
    else:
        return False           

    
def clearLabel():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    

root = tk.Tk()
#root.geometry('400x200')
root.minsize(400,300)     # See the difference between the two :(
#root.resizable(False, False)

root.columnconfigure(0, weight=1)

frame = ttk.Frame(root)
frame.grid(row=0,column=0, sticky="EW", padx=5, pady=10)
frame.columnconfigure(0, weight=1)

# Display Label for 'Name'

label_name = ttk.Label(frame, text='Name', background='yellow')
label_name.grid(row=0, column=0, sticky="EW")

entry_name = ttk.Entry(frame, width=50)
entry_name.grid(row=0, column=1)
entry_name.focus()


# Display Label for 'Age'

label_age = ttk.Label(frame, text='Age', background='orange')
label_age.grid(row=1, column=0, sticky="EW")

entry_age = ttk.Entry(frame, width=50)
entry_age.grid(row=1, column=1)


# Display Label for 'Phone Number'

label_phone = ttk.Label(frame, text='Phone', background='orange')
label_phone.grid(row=2, column=0, sticky="EW")

entry_phone = ttk.Entry(frame, width=50)
entry_phone.grid(row=2, column=1)


# Display Label for 'Address'

label_address = ttk.Label(frame, text='Address', background='blue')
label_address.grid(row=3, column=0, sticky="EW")

entry_address = ttk.Entry(frame, width=50)
entry_address.grid(row=3, column=1)


# Button to submit and retrieve records

frame2 = ttk.Frame(root)
frame2.grid(row=1, column=0, sticky="EW")
frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)

submit_button = ttk.Button(frame2, text="Submit the record", comman=submitRecord)
submit_button.grid(row=0, column=0, sticky="EW")

retrieve_record = ttk.Button(frame2, text="Retrieve the record",command=retrieveRecord)
retrieve_record.grid(row=0, column=1, sticky="EW")

update_record = ttk.Button(frame2, text="Update",command=update)
update_record.grid(row=1, column=0, sticky="EW")

quit_program = ttk.Button(frame2, text="Quit",command=root.destroy)
quit_program.grid(row=1, column=1, sticky="EW")


delete_record = ttk.Button(frame2, text="Delete Record",command=deleteRecord)
delete_record.grid(row=2, column=1, sticky="EW")

record_number = tk.IntVar()
number_of_records = ttk.Label(frame2, textvariable = record_number)
number_of_records.grid(row=2, column=0, sticky="EW")


# Label to display the retrieved record inside 'Root' itself

display = tk.StringVar()
frame3 = ttk.Frame(root)
frame3.grid(row=2, column=0, sticky="EW")
frame3.columnconfigure(0, weight=1)

display_screen = ttk.Label(frame3, textvariable = display)
display_screen.grid(sticky="EW")


root.mainloop()
print('Program Exit')
