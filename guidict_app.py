import tkinter as tk
import json #imported json lib
from difflib import get_close_matches #imported get_close_matches from difflib

window = tk.Tk()
window.geometry("700x400")
window.title("Dictionary")

data = json.load(open("data.json")) #Opened data.json file and loaded it into a 'data' variable
ynfield = tk.Entry()

def dictionary(w): #def
    if w in data: #checks if the user input is in the loaded data or not, returns True or False
        if (len(data[w]) >= 1):
            tresult = tk.Text(master=window, height= 20, width=60)
            tresult.grid(column=1, row = 3)
            for i in range(0,len(data[w])): #This loop is for iterating through the multiple definitions of a word and printing them in each seperated line
                #tresult.insert(tk.END, ("Def", i+1, ":", data[w][i], "\n")) # { } are present after everyline.
                tresult.insert(tk.END, ("Def {} : {} \n".format(i+1, data[w][i])))

    elif w.title() in data:
        if (len(data[w.title()]) >= 1):
            tresult = tk.Text(master=window, height= 15, width=60)
            tresult.grid(column=1, row = 3)
            for i in range(0,len(data[w.title()])): #This loop is for iterating through the multiple definitions of a word and printing them in each seperated line
                #print("Def", i+1, ":", data[w.title()][i])

                tresult.insert(tk.END, ("Def {} : {} \n".format(i+1, data[w.title()])))

    elif (len(get_close_matches(w, data.keys())) > 0):
        option = str("Are you looking for '%s'? Y or N: " % get_close_matches(w, data.keys())[0])
        ynlabel = tk.Label(text=option)
        ynlabel.grid(column=0, row=2)

        ynfield.grid(column=1, row =2)

        ynbutton = tk.Button(text="Enter", command = ynvalue)
        ynbutton.grid(column=3, row=2)


    else:
        tresult = tk.Text(master=window, height= 20, width=60)
        tresult.grid(column=1, row = 3)
        tresult.insert(tk.END, "Sorry! There is no meaning for {} .".format(w))

#(dictionary(get_value())) #Def call
alabel = tk.Label(text="Enter your word")
alabel.grid(column=0, row=0)

tfield = tk.Entry()
tfield.grid(column=1, row =0)

#tresult = tk.Text(master=window, height= 4, width=50)
#tresult.grid(column=1, row = 3)


def get_value():
    res = str(tfield.get())
    dictionary(res.lower())

def ynvalue():

    yn = str(ynfield.get())
    word = str(tfield.get()).lower()
    if yn == 'Y':
        tresult = tk.Text(master=window, height= 20, width=60)
        tresult.grid(column=1, row = 3)
        if (len(data[get_close_matches(word, data.keys())[0]]) > 1):

            for i in range(0, len(data[get_close_matches(word, data.keys())[0]])): #This loop is for iterating through the multiple definitions of a word and printing them in each seperated line
                #print("Def", i+1, ":", data[get_close_matches(w, data.keys())[0]][i])

                tresult.insert(tk.END, ("Def {} : {} \n".format( i+1, data[get_close_matches(word, data.keys())[0]][i] )) )

    elif yn == 'N':
        tresult = tk.Text(master=window, height= 20, width=60)
        tresult.grid(column=1, row = 3)
        tresult.insert(tk.END, 'Sorry! We could not find the definition for your word.')

    else:
        #print("Please select either 'Y' or 'N'")
        tresult = tk.Text(master=window, height= 20, width=60)
        tresult.grid(column=1, row = 3)
        tresult.insert(tk.END, "Inappropirate selection!")



tbutton = tk.Button(text="Enter", command=get_value)
tbutton.grid(column=2, row=0)



window.mainloop()
