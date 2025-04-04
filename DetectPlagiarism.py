# Import required library
from tkinter import *

# First we need to read the contents of two files
with open('File_1.txt') as f1:
    s1 = f1.read().lower().split()
    l1 = [i for i in s1 if i.isalnum()]

with open('File_2.txt') as f2:
    s2 = f2.read().lower().split()
    l2 = [i for i in s2 if i.isalnum()]

# Finding how many words are common in two files
plag_words = len(set(l1).intersection(set(l2)))

# Finding total number of words in two files
total_words = len(l1) + len(l2)

# Check if total_words is zero to prevent division by zero
if total_words == 0:
    plag_percent = 0  # If no words in both files, set plagiarism percentage to 0
else:
    # Formula to calculate the plagiarism percent
    plag_percent = 100 - round((total_words - plag_words * 2) / total_words * 100)

# Displaying the result
result = "The Plagiarized Content Percent among two files is " + str(plag_percent) + "%"

# Create a window
win = Tk()
win.geometry("800x200")

# Set background color based on plagiarism percent
if plag_percent >= 30 and plag_percent <= 60:
    bg_color = "Yellow"
else:
    bg_color = "Red"

canvas = Canvas(win, width=700, height=200, bg=bg_color)
canvas.create_text(350, 100, text=result, fill="black", font=('Helvetica', 15, 'bold'))
canvas.pack()

win.mainloop()
