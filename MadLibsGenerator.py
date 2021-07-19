"""A GUI Based MadLibs Generator."""

# importing the modules which needed
from tkinter import *
import time

# Global Variables
RED = "#f03c3c"
GREEN = "#3cf069"
BLUE = "#3c8af0"
BLACK = "#080808"
YELLOW = "#ddeb4b"
WHITE = "#ffffff"

# Main function (this is the main engine of this generator)
def madLibs_1():
    """Main function of generator...."""
    name = input("Enter your name: ")
    place = input("Enter a place: ")
    tool = input("Enter a tool name used to repair the car: ")
    animal = input("Enter a animal name: ")
    food = input("Enter the name of the food which you like: ")
    website = input("Enter the name of the website which you visit the most: ")
    laptop = input("Enter the name of the laptop which you like the most: ")
    book = input("Enter the name of the novel which you have read: ")
    person = input("enter the name of a famous person: ")
    print("Your name is "+ name + "you like to visit "+ food + "." + "You are going to read "+ tool + "There is a animal in the zoo which you have ride whose name is "+ animal + "you like to see the films of " + person + "you have made "+website + "you have bought "+ laptop)

# creating the main window with tkinter
root = Tk()
root.title("Madlibs Generator")
root.geometry("400x400")
mainLabel = Label(root, text="Mad Libs Generator", bg=GREEN, fg=WHITE, font=('Helvetica', 16, 'bold'))
mainLabel.pack()
mainButton = Button(root, text="Generate", bg=BLUE, fg=WHITE, font=('Helvetica', 16, 'bold', 'italic'), command=madLibs_1)
mainButton.pack()
root.mainloop()