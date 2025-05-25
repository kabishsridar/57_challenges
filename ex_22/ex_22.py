first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))


if first > second and first > third:
    print(f"The largest number is {first}")
elif second > third and second > first:
    print(f"The largest number is {second}")
elif third > second and third > first:
    print(f"The largest number is {third}")