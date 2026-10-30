# The most suprising thing for me was how lists are sorted, since their order is kinda messy
# when I was choosing a car - I could have uploaded all the info into a database and used list as a way to sort information

print("---Exercise 1: Build the list ---")

inventory = ["pen","notebook","stapler", "tape","marker"]
print(inventory)
print(len(inventory))

print("---Exercise 2: index practice ---")
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

print("---Exercise 3: slicing practice ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("---Exercise 4: modifying the list ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)

inventory.append("Zoo")
inventory.append("zoo")
inventory.append("1")
inventory.append("%")
inventory.sort()
print(inventory)

print("--- exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")
print(coords)

print("--- exercise 6: Average List of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f'Total: {total}')
print(f'Count: {count}')
print(f'Average: {average}')
print(f'Best: {max(sales)}')
print(f'Worst: {min(sales)}')

print("--- exercise 7: accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * 0.9, 2))

print("Original prices:", prices)
print("Discounted prices:", discount)

print("--- exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High Sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")