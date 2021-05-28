import tkinter as tk
from tkinter import filedialog, Text
import os
import webbrowser
import sys
import subprocess
import csv
import numpy as np
import math
import random
import operator
import itertools
import pickle
import json
from flask import render_template
from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import PorterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('punkt')

data = []
datain=[]
dataout=[]
datarem=[]
item_names = {}
item_names2 = {}

app = Flask(__name__)



root = tk.Tk()
apps=[]


# filename = "trial.csv"

def load_items(filename):
	total_items = 0
	with open(filename, 'r', encoding='UTF8') as csvfile:
		csvreader = csv.reader(csvfile)
		# Skip header
		next(csvreader)
		for row in csvreader:
			if not row[0] in item_names:
				item_names[total_items] = row
				total_items += 1
	print ("Loaded:"+str(item_names)+" items")
	
    

load_items('trial.csv')
with open('trial2.json', 'w') as f:
    json.dump(item_names, f)
# load_items('addresses.csv')


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/bin", title="Selected Files"),
    # fileTypes=(("executables","*exe"),("all files","*.*"))
    
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    # for app in apps:
    #     subprocess.call(["xdg-open", app]) 
    print ("Loaded:"+str(data)+" items")

# # actual screen
# canvas = tk.Canvas(root, height=700, width = 700, bg="#263D42")
# canvas.pack()

# # white thing in the middle
# frame=tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# buttons
# openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
# openFile.pack()

# runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42",command=runApps)
# runApps.pack()






@app.route('/')
def my_form_post():

    newWord = item_names

    return render_template("index.html", apis=newWord)

# openCsv = tk.Button(root, text="Open Apps", padx=10, pady=5, fg="white", bg="#263D42",command=my_form_post())
# openCsv.pack()
# root.mainloop()

if __name__ == "__main__":
    print("Starting server...")
    app.run(debug=True)