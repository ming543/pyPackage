
import Tkinter as tk

class showbox():

#Check box
      def textbox(self, s):   
        win = tk.Tk()
        win.title("Check BOK")
        win.geometry("500x100+500+300")
        label = tk.Label(win, font=('Arial', 16), text= str(s) )
        label.pack()
        button=tk.Button(win, text="OK", bg="green", command=quit)
        #button.geometry("50x50")
        button.pack()
        win.mainloop()
