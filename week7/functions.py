#self assesment
#The fisrt bug I spotted was the missing column - once I ran the program
#  I got a suggestion to fix that in terminal
#apply discount gets the discount for each specific tier 
# (once u know the tier you can automatically apply the discount)
#Right now the code is simple and understandable, but in the future explanation could be needed
#I only used AI for the debbuging task and it helped for the understanding  

#----ex1-----

def calculate_tax(price, rate):
    return price*rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")

#-----ex2------

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.9
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

#-----ex3-------

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"after gold discount: ${discounted:.2f}")
print(f"after Tax: ${after_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

#---------ex 4 --------------

orders = [(200, "gold"), (10, "silver"), (80, "bronze"), (500, "none")]

for price , tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

#-----ex6------

x = 100
def double_it():
    x = 999 # could do global x 
    return x * 2
print(x)
print(double_it())
print(x)

#-----ex5------