import time, os
import Tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup



def box(s):
    #Check box
    win = tk.Tk()
    win.title("Check BOK")
    win.geometry("500x100+500+300")
    label = tk.Label(win, font=('Arial', 16), text='Connect loopback cable ' + str(s) )
    label.pack()
    button=tk.Button(win, text="OK", bg="green", command=quit)
    #button.geometry("50x50")
    button.pack()
    win.mainloop()

box(485)

