
# Create a shopping cart programme that will continuously ask the user for a food product and the price of that product
# Have an exit clause if the user wishes to stop adding more things to their cart
# At the end show the food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food == 'q':
        break
    price = float(input(f"Enter the price for {food}: R"))
    foods.append(food)
    prices.append(price)

print("Your shopping cart contains:")
for food, price in zip(foods, prices):
    print(f"- {food}: R{price:.2f}")
print(f"Total cost: R{sum(prices):.2f}")
