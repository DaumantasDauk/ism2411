#----ex1------
# download the data

#----ex2------
import csv

with open('data/sales.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#---ex3------
with open("data/sales.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

#---ex4------
with open("data/sales.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        product, price_str, quantity_str = row
        price = float(price_str)
        quantity = int(quantity_str)
        add_total = price * quantity
        total_revenue =+ add_total
        print(f'{product}: {quantity} units x ${price:.2f} = ${add_total:.2f}')
print(f"Overall Total Revenue: ${total_revenue:,.2f}")

#---ex5------
original_count = 0
written_count = 0
with open("data/sales.csv", newline="") as infile, open(
    "data/cleaned.csv", mode="w", newline=""
) as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        original_count += 1
        product2, price_str2, qty_str2 = row
        price = float(price_str2)
        qty = int(qty_str2)
        total2 = price * qty
        writer.writerow([product2, price, qty, total2])
        if total2 > 100:
            writer.writerow([product2, price, qty, total2])
            written_count += 1
print(f"Original rows present: {original_count}")
print(f"rows written to cleaned.csv: {written_count}")

#----ex6------
dict_total_revenue = 0
with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        dict_total_revenue += line_total
print(f"DictReader Total Revenue: ${dict_total_revenue:,.2f}")

#Dict Reader helps with code readability or if the collumns changes places
#standart reader is preffered for simple files  

#----ex7------
print("EX7 STARTS HERE")
product_summary = {}
with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        if product in product_summary:
            product_summary[product] += line_total
        else:
            product_summary[product] = line_total
for product in sorted(product_summary.keys()):
    revenue = product_summary[product]
    print(f"{product}: ${revenue:,.2f}")

#----ex8------
from datetime import datetime
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", mode="a", newline="") as log_file:
    log_file.write(f"Run at {current_time} - Total Revenue: ${total_revenue:,.2f}\n")
print("Time added")