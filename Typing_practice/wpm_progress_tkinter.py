import tkinter as tk # importing the modules
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

def graph(categories, values): # function to display graph, it takes categories and values as a parameters
    plt.bar(categories, values) # to plot the bar graph
    plt.title('WPM progress for this weeek') # title of the window
    plt.xlabel('Days') # The label for x axis
    plt.ylabel('WPM') # The label for Y axis
    plt.show() # displays the graph

if __name__ == "__main__": # block to start first
    fin = open('progress.txt', 'r') # opening the file in read mode
    data = fin.read() # reads all the lines in the string format
    lst = data.split() # splitting them and converting to list
    categories_lst = [] # initiating two empty lists
    values_lst = []
    for i in range(len(lst)): # append the days number to the categories list and the wpm to the values list
        if i % 2 == 0:
            categories_lst.append(lst[i])
        else:
            values_lst.append(int(lst[i]))

    root = tk.Tk() # using Tk class and storing it
    root.title('WPM Progress') # window title
    root.geometry("700x600") # size of the window

    button = tk.Button(root, text="display graph", command=lambda: graph(categories_lst, values_lst)).pack(pady=0) # button to display the graph
    root.mainloop()