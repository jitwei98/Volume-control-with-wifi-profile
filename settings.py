from Tkinter import *
from ver1 import SSID

def savetofile():
	SSID().add_entry(entry.get(), int(vol.get()))

root = Tk()

root.title("sTFU")

label_1 = Label(root, text = "SSID")
label_2 = Label(root, text = "Volume")
entry = Entry(root)
vol = Spinbox(root, from_=0, to=100)
save = Button(root, text="Save", command=savetofile)

label_1.grid(row=0, sticky=E, padx=0)
label_2.grid(row=1, sticky=E, padx=5)
entry.grid(row=0, column=1)
vol.grid(row=1, column=1)
save.grid(row=2, column=1, sticky=E, padx=10, pady=5)

# put current SSID
entry.insert(END, SSID().get_SSID())


root.mainloop()