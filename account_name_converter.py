import os
from os import path
from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Convert Account Numbers to Account Names")
root.geometry('325x250')

account_names = {
'6001' : 'COMPANY A',
'6002' : 'COMPANY B',    
'6005' : 'COMPANY C',
'6006' : 'COMPANY D',
'6011' : 'COMPANY E',
'6013' : 'COMPANY F',
'6014' : 'COMPANY G',
'6015' : 'COMPANY H',
'6016' : 'COMPANY I',
'6018' : 'COMPANY J',
'6020' : 'COMPANY K',
'6022' : 'COMPANY L',
'6025' : 'COMPANY M',
'6026' : 'COMPANY N',
'6027' : 'COMPANY O',
'6036' : 'COMPANY P',
'6038' : 'COMPANY Q',
'6041' : 'COMPANY R',
'6042' : 'COMPANY S',
'6043' : 'COMPANY T',
'6044' : 'COMPANY U',
'6046' : 'COMPANY V',
'6047' : 'COMPANY W'
}

# Create folders
paste_folder = path.exists('files')
convert_folder = path.exists('fileChange')
send_folder = path.exists('filesToSend')

if paste_folder == False:
    os.mkdir('files')
if convert_folder == False:
    os.mkdir('fileChange')
if send_folder == False:
    os.mkdir('filesToSend')

# Function to convert file names
def acc_numbers():
    # Get list of files from directory and 
    # get last file for progress bar
    file_list = os.listdir('files')
    last_file = file_list[-1]
    x = len(file_list)
    y = 100/x
    
    # Cut names so that only Account number remain
    for filename in file_list:
        old = f"files/{filename}"
        new = f"fileChange/{filename[6:10] + '.pdf'}"
        my_progress_filenumber['value'] += y
        root.update_idletasks()
        time.sleep(0.2)
        if filename == last_file:
            status_filenumber.config(text="Finished", bg='green')
        else:
            status_filenumber.config(text=F"{filename} changed to... {filename[6:10] + '.pdf'}")
        os.rename(old, new)

    # Change file name from Account number to Account name
    file_changed_list = os.listdir('fileChange')
    last_changed_file = file_changed_list[-1]
    x2 = len(file_changed_list)
    y2 = 100/x

    for changed_filename in file_changed_list:
        try:
            old = f"fileChange/{changed_filename}"
            name = account_names.get(changed_filename[0:4])
            new = f"filesToSend/{name + '.pdf'}"
            # Progress bar
            my_progress_filename['value'] += y2
            root.update_idletasks()
            time.sleep(0.2)
            if changed_filename == last_changed_file:
                status_filename.config(text="Finished", bg='green')
            else:
                status_filename.config(text=" ")
                status_filename.config(text=F"{changed_filename[0:4]} changed to...{name + '.pdf'}")
            os.rename(old, new)
        except TypeError:
            pass

# Convert button
convert_button = Button(root, text="Change Names", width=30, command=acc_numbers)
convert_button.grid(row=0, column=0, pady=(10,0))

# Slice to number
number_label = Label(root, text='Convert to Account Number')
number_label.grid(row=1, column=0, padx=(10,0), pady=(10,0))

my_progress_filenumber = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
my_progress_filenumber.grid(row=2, column=0, padx=(10,0))

status_filenumber = Label(root, text="...", width=42, borderwidth=1, relief=SOLID)
status_filenumber.grid(row=3, column=0, padx=(10,0), pady=(5,0))

# Number to Name
name_label = Label(root, text='Convert to Account Name')
name_label.grid(row=4, column=0, padx=(10,0), pady=(10,0))

my_progress_filename = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
my_progress_filename.grid(row=5, column=0, padx=(10,0))

status_filename = Label(root, text="...", width=42, borderwidth=1, relief=SOLID)
status_filename.grid(row=6, column=0, padx=(10,0), pady=(5,0))

exit_button = Button(root, text="Exit", width=30, command=root.quit)
exit_button.grid(row=7, column=0, pady=(10,0))

root.mainloop()


