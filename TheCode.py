import pafy
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image  # pip install Pillow
import secrets
import string

screen = tk.Tk()
screen.geometry('500x300')
screen.title('Youtuber Downloader')
screen["bg"] = "light slate gray"

image1 = Image.open("logo1.png")
image1 = image1.resize((120,30), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=200, y=25)

def saveLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()

def Download():
    url = str(linkdata.get())
    if (len(url) > 1):
        #Folder_Name = filedialog.askdirectory()
        video = pafy.new(url)
        streams = video.streams
        best = video.getbest()
        best.download(Folder_Name)
        bestExtension = best.extension
        bestResolution = best.resolution
        linkdata.delete(0, END)
        myLabel2 = Label(screen, text="Download completed! "+bestResolution+" "+bestExtension, font=("Verdana  8 bold"), fg="blue")
        myLabel2.place(x=160, y=70)
    else:
        messagebox.showerror("error", "Enter Youtube Link!")

myLabel = Label(screen, text="Enter Link:", font=('Arial', 12) )
myLabel.place(x=60, y=100)

linkdata = Entry(screen, width=50, bd=4)
linkdata.place(x=150, y=100)

# choosePath Button hover style function
def on_enter4(e):
    saveEntry['bg'] = 'ivory2'
def on_leave4(e):
    saveEntry['bg'] = 'gray73'
saveEntry = Button(screen, text="Choose Path", pady=4, bd=2, width=10, font=('Arial', 10, 'bold'), bg='gray73', activebackground ="green", command=saveLocation)
saveEntry.place(x=180, y=140)
saveEntry.bind("<Enter>", on_enter4)
saveEntry.bind("<Leave>", on_leave4)

# Download Button hover style function
def on_enter3(e):
    btn['bg'] = 'ivory2'
def on_leave3(e):
    btn['bg'] = 'gray73'
btn = tk.Button(screen, text ="Download", pady=4, bd=2, width=10, font=('Arial', 10, 'bold'), bg='gray73', activebackground ="green", command=Download)
btn.place(x=280, y=140)
btn.bind("<Enter>", on_enter3)
btn.bind("<Leave>", on_leave3)

# EXIT Button hover style function
def on_enter2(e):
    exit_Button['bg'] = 'gray30'
def on_leave2(e):
    exit_Button['bg'] = 'gray73'

# Exit Button
exit_Button = tk.Button(screen, text="EXIT", width=10, height=1, bd=10, font=("Arial", 12, "bold"), bg='gray73', activebackground ="red", command=screen.destroy)
exit_Button.place(x=350, y=230)
exit_Button.bind("<Enter>", on_enter2)
exit_Button.bind("<Leave>", on_leave2)

screen.mainloop()