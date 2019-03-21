""" Denne python fil er en eksempel løsning på GUI opgaverne fra
lektion 7. Der kan være andre varianter at løse opgaverne på, men dette
er mit bud"""

import tkinter as tk

def change():
    #code here
    input = entry.get()
    label.config(text=str(input))

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Hej, velkommen til mit program\n\n\n")
label.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack()
button2 = tk.Button(frame,
                   text="Change text",
                   command=change)
button2.pack()
#button.pack(side=tk.BOTTOM)


S = tk.Scrollbar(frame)
T = tk.Text(frame, height=4, width=50)

S.config(command=T.yview)
T.config(yscrollcommand=S.set)
S.pack(side=tk.RIGHT,fill=tk.Y, )
T.pack(fill=tk.Y, side=tk.LEFT)

quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(tk.END, quote)


frame2 = tk.Frame(root)
frame2.pack()

label2 =  tk.Label(frame2, text="Indtast navn:")
label2.pack(side=tk.LEFT,padx= 10, pady=10)
entry = tk.Entry(frame2)
entry.pack(side=tk.LEFT,padx= 10, pady=10)


root.mainloop()