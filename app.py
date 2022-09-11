import tkinter as tk
from tkinter import filedialog, Text
import os

#create root
root = tk.Tk()
apps = []
#create savefile
if os.path.isfile('apps/GUIApp/save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
#define button acts
#add App
def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/desktop", title='Select File',
    filetypes=(('Exe', "*.exe"), ('all files',"*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()
#run App
def runApp():
    for app in apps:
        os.startfile(app)

#create canvas
canvas = tk.Canvas(root, height=350, width=350, bg="#263D42")
canvas.pack()
frame = tk.Frame(root, bg='white')
frame.place(relheight=0.6, relwidth=0.6, relx=0.2, rely=0.1)
#create buttons
openFile = tk.Button(root, text='Open File', padx=10,pady=5, bg="#263D42", command=addApp)
openFile.pack()
runApps = tk.Button(root, text='Run Apps', padx=10,pady=5, bg="#263D42", command=runApp)
runApps.pack()
#program running
for app in apps:
    label = tk.Label(frame, text = app)
root.mainloop()
#save log
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')