
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


# Exercise 4 - Compute Totals

total_revenue = 0

with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header

    for row in reader:
        product, price, quantity = row

        # Convert strings to numbers
        price = float(price)
        quantity = int(quantity)

        # Calculate revenue for this sale
        revenue = price * quantity
        total_revenue += revenue

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

# Print overall revenue
print(f"Total revenue: ${total_revenue:.2f}")


# Exercise 5 - Filter and Write Cleaned CSV

original_count = 0
cleaned_count = 0

# Open the original CSV and create the cleaned CSV
with open("data/sales.csv", "r", newline="", encoding="utf-8") as input_file:
    reader = csv.reader(input_file)
    next(reader)  # Skip header

    with open("data/cleaned.csv", "w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)

        # Write the new header
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            product, price, quantity = row

            price = float(price)
            quantity = int(quantity)
            total = price * quantity

            original_count += 1

            # Keep only orders above $100
            if total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
                cleaned_count += 1

# Print results
print(f"Original orders: {original_count}")
print(f"Cleaned orders: {cleaned_count}")



# Exercise 6 - csv.DictReader

dict_total_revenue = 0

with open("data/sales.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        revenue = price * quantity
        dict_total_revenue += revenue

        print(f"{product}: {quantity} units x ${price:.2f} = ${revenue:.2f}")

print(f"DictReader total revenue: ${dict_total_revenue:.2f}")

# csv.reader is useful for simple files because it accesses columns by position.
# csv.DictReader is better for business records because it uses column names.
