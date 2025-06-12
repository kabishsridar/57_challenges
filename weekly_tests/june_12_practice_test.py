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

    for data in lst1:
        current_category = data[1]
        current_amount = float(data[2])

        if current_category in category_sums:
            category_sums[current_category] += current_amount
            category_counts[current_category] += 1
        else:
            category_sums[current_category] = current_amount
            category_counts[current_category] = 1

    category_list = []
    average_list = []

    for category in distinct_categories:
        if category in category_sums and category_counts[category] > 0:
            calculated_average = category_sums[category] / category_counts[category]
            category_list.append(category)
            average_list.append(calculated_average)

    plt.bar(category_list, average_list)
    plt.title('Average amounts of each categories:')
    plt.show()
if __name__ == "__main__":
    print(type(argv))
    print(f"script: {argv[0]}")
    print(f"input file: {argv[1]}")
    plot_average(argv[1])