
# Lucas Camargo Morschel
# ISM2411 - Python for Business
# Lab 12 - Read a Sales CSV, Write a Cleaned Report

import csv

# Exercise 2 - Read and Print Raw Rows

with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Exercise 3 - Skip the Header

with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    # Save and skip the header
    header = next(reader)

    # Print the header separately
    print("Header:", header)

    # Print only the data rows
    for row in reader:
        print(row)
