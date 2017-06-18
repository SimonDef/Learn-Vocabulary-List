#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:35:52 2017

@author: simondefrenet
"""

import random

WORDLIST_FILENAME = "French words - Sheet2Fr.csv"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    lbl_nbwords.configure(text="Loading word list from file...")
    lbl_nbwords.pack()
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline().strip() # get the first line in line
    word = line.split(',')
    global language1
    global language2
    language1=word[0]
    language2=word[1]
    lbl_language1.configure(text=language1)
    lbl_language2.configure(text=language2)
    lbl_language1.pack(fill=tk.X)
    lbl_language2.pack(fill=tk.X)
    guangdongwa_dictionnary=[]
    line = inFile.readline().strip() # get the first line in line
    i=0
    while line:
        word = line.split(',')
        guangdongwa_dictionnary+=[word]
        line = inFile.readline().strip() # get the next line in line
        i+=1
    # wordlist: list of strings
    lbl_nbwords.configure(text="  %s words loaded." %str(i))
    return guangdongwa_dictionnary

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

def translate(to_language):
    testword=chooseWord(guangdongwa_dictionnary)
    if to_language==language1:        
        lbl_question.configure(text='How do you say "%s" in %s ? '% (testword[1],language1))
        return testword[0]
    else:
        lbl_question.configure(text='How do you say "%s" in %s ? '% (testword[0],language2))
        return testword[1]
        
import tkinter as tk

window = tk.Tk()
window.title("learnvocab")
window.geometry("600x600")
lbl_welcome = tk.Label(window, text="Welcome to the game to learn vocabulary!")
lbl_welcome.pack()
lbl_language1 = tk.Label(window)
lbl_language2 = tk.Label(window)
lbl_nbwords=tk.Label(window)
guangdongwa_dictionnary = loadWords()
options=['one','two','three','four']

btn_next=tk.Button(window, state='active')
btn_next.configure(text="Next question")
btn_next.configure(command= lambda: display_question())
btn_next.pack()

lbl_question = tk.Label(window, text="question here")
lbl_question.pack()
ent_reply = tk.Label(window)

ent_guess= tk.Entry(window)
ent_guess.pack()

btn=tk.Button(window, state='active',text="Validate your guess",command= lambda: check_result(correct_guess))
btn.pack()

lbl_result = tk.Label(window, text="result here")
lbl_result.pack()

window.mainloop()

def display_question():
    #test=random.choice(["english","cantonese","chooseenglish","choosecantonese"])
    global correct_guess
    lbl_result.configure(text="")
    ent_guess.delete(0,100)	
    test=random.choice([language1,language2])
    correct_guess=translate(test)
    
def check_result(correct_guess):
    result=ent_guess.get()
    if result==correct_guess:
        lbl_result.configure(text="Well Done")
    else:
        lbl_result.configure(text="Not this time, it was %s. Try again" % correct_guess)

'''
    elif test=="chooseenglish":
        choose("english")
    elif test=="choosecantonese":
        choose("cantonese")
'''
        