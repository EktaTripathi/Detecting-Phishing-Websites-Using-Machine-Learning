import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import preprocess as pre
import RandomForest as RF
import logisticRegression as LR
import SupportVectorMachine as SV
#from sklearn.externals import joblib
import inputScript
import joblib

bgcolor="#6dc1f2"
bgcolor1="#eff7be"
fgcolor="black"


def Home():
	global window
	def clear():
	    print("Clear1")
	    txt.delete(0, 'end')
	    txt1.delete(0, 'end')



	window = tk.Tk()
	window.title("Detecting Phising Website")
 
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen',True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	

	message1 = tk.Label(window, text="Detecting Phising Website" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'bold underline'))
	message1.place(x=100, y=20)

	lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=100, y=200)
	
	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=400, y=215)

	lbl1 = tk.Label(window, text="Enter URL",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=100, y=300)
	
	txt1 = tk.Entry(window,width=40,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=400, y=315)

	def browse():
		path=filedialog.askopenfilename()
		print(path)
		txt.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Train Dataset")	

	def preproc():
		sym=txt.get()
		if sym != "" :
			pre.process(sym)
			print("preprocess")
			tm.showinfo("Input", "Preprocess Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset")

	def RFprocess():
		sym=txt.get()
		if sym != "" :
			RF.process(sym)
			tm.showinfo("Input", "RANDOM FOREST Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset")

	def LRprocess():
		sym=txt.get()
		if sym != "" :
			LR.process(sym)
			tm.showinfo("Input", "LogisticRegression Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset")
	

	def SVMprocess():
		sym=txt.get()
		if sym != "" :
			SV.process(sym)
			tm.showinfo("Input", "SVM Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset")

	def Predicted():
		sym=txt1.get()
		if sym != "" :
			#load the pickle file
			classifier = joblib.load('final_models/rf_final.pkl')
			#checking and predicting
			checkprediction = inputScript.process(sym)
			prediction = classifier.predict(checkprediction)
			print(prediction)
			tm.showinfo("Input", "Predicted Class is  "+ str(prediction[0]))
		else:
			tm.showinfo("Input error", "Select Dataset")

	browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse.place(x=650, y=200)

	clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
	clearButton.place(x=950, y=200)
	 
	proc = tk.Button(window, text="Preprocess", command=preproc  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	proc.place(x=30, y=600)
	

	RFbutton = tk.Button(window, text="RANDOM FOREST", command=RFprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	RFbutton.place(x=220, y=600)


	SVMbutton = tk.Button(window, text="SVM", command=SVMprocess  ,fg=fgcolor   ,bg=bgcolor1 ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	SVMbutton.place(x=420, y=600)

	LRbutton = tk.Button(window, text="LogisticRegression", command=LRprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	LRbutton.place(x=600, y=600)

	PRbutton = tk.Button(window, text="Prediction", command=Predicted  ,fg=fgcolor   ,bg=bgcolor1   ,width=16  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	PRbutton.place(x=800, y=600)


	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=1000, y=600)

	window.mainloop()
Home()

