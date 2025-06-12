import matplotlib.pyplot as plt # importing matplotlin to display the bar graph
import csv # importing csv
from sys import argv
def plot_average(filename):
    fin = open(f'{filename}', 'r') # opening the csv file in read mode
    reader = csv.reader(fin) # reading the csv file and stores in the type of csv.reader
    lst = [] # initiating lst as an empty list to typecast the data read from csv.reader to list
    for i in reader:
        lst.append(i)

    lst1 = lst[1:] # storing all the values except the first one which i category
    amounts = [] # initiating empty lists
    category = []

    for row in lst1: # loop through each categories
        category.append(row[1]) # appending categories to initiated list
        amounts.append(row[2])
    distinct_categories = list(set(category)) # initiating distinct_categories as an empty list to find the distinct categories 

    category_sums = {} # initiating empty dictionaries
    category_counts = {}

    for data in lst1: # loop through each categories
        current_category = data[1]
        current_amount = float(data[2]) # converting amount to float

        if current_category in category_sums:
            category_sums[current_category] += current_amount # adding amount to existing sum
            category_counts[current_category] += 1 # incrementing the count
        else:
            category_sums[current_category] = current_amount  # do not increment
            category_counts[current_category] = 1

    category_list = [] # initiating category_list as an empty list
    average_list = [] # initiating average_list as an empty list

    for category in distinct_categories: # loop through distinct categories
        if category in category_sums and category_counts[category] > 0:
            calculated_average = category_sums[category] / category_counts[category]  # calculating average
            category_list.append(category) # appending category to list
            average_list.append(calculated_average) # appending calculated average

    plt.bar(category_list, average_list) # plots the bar graph of averages for each category
    plt.title('Average amounts of each categories:') 
    plt.show() # displays the graph
if __name__ == "__main__": # this should execute at first
    print(type(argv))
    print(f"script: {argv[0]}")
    print(f"input file: {argv[1]}") # in the command prompt we need to run the file with the syntax python june_12_practice_test.py sample_expenses.csv
    plot_average(argv[1]) # calling the function