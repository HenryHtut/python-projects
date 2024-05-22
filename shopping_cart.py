#Shopping cart program 

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quite) :")
    if food.lower() ==  "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food) 
        prices.append(price)  

print("------Your Cart-----")
for x in foods:
    print(x, end=" ")

for y in prices:
    total += y
print()
print(f"Your total is: ${total}")


