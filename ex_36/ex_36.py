import math

array = []  # Store response times

while True:
    prompt = input("Enter a number: ")
    if prompt.lower() == "done":
        break
    else:
        array.append(int(prompt))

print(f"Numbers: {', '.join(map(str, array))}")

def find_avg(lst):
    total = sum(lst)  # Compute sum of all values
    mean = total / len(lst)  # Compute mean
    print(f"The average is {mean:.2f}")

def find_min_max(lst):
    print(f"The minimum is {min(lst)}")
    print(f"The maximum is {max(lst)}")

def find_std_dev(lst, mean):
    squared_diffs = [(x - mean) ** 2 for x in lst]  # Compute squared differences
    variance = sum(squared_diffs) / len(lst)  # Compute variance
    std_dev = math.sqrt(variance)  # Compute standard deviation
    print(f"The standard deviation is {std_dev:.2f}")

# Compute statistics
find_avg(array)
find_min_max(array)

mean = sum(array) / len(array)  # Mean value needed for standard deviation calculation
find_std_dev(array, mean)