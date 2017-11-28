import json #imported json lib
from difflib import get_close_matches

data = json.load(open("data.json")) #Opened data.json file and loaded it into a 'data' variable

word = (input("Enter your word: ")) #Asking user for input

def dictionary(w): #def
    if w in data: #checks if the user input is in the loaded data or not, returns True or False
        if (len(data[w]) >= 1):
            for i in range(0,len(data[w])): #This loop is for iterating through the multiple definitions of a word and printing them in each seperated line
                print("Def", i+1, ":", data[w][i])
    elif w.title() in data:
        if (len(data[w.title()]) >= 1):
            for i in range(0,len(data[w.title()])): #This loop is for iterating through the multiple definitions of a word and printing them in each seperated line
                print("Def", i+1, ":", data[w.title()][i])

    elif (len(get_close_matches(w, data.keys())) > 0):
        option = input("Are you looking for '%s'? Y or N: " % get_close_matches(w, data.keys())[0]).upper()
        if option == 'Y':
            if (len(data[get_close_matches(w, data.keys())[0]]) > 1):
                for i in range(0,len(data[get_close_matches(w, data.keys())[0]])): #This loop is for iterating through the multiple definitions of a word and printing them in each seperated line
                    print("Def", i+1, ":", data[get_close_matches(w, data.keys())[0]][i])

        elif option == 'N':
            print('Sorry! We could not find the definition for your word.')

        else:
            #print("Please select either 'Y' or 'N'")
            print("Inappropirate selection!")

    else:
        print('Sorry! There is no meaning for', w,".")

(dictionary(word.lower())) #Def call
