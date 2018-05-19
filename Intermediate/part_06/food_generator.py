import random

food = ['Macaroni', 'Chicken', 'Spaghetti', 'Fish', 'Eggs', 'Sausage', 'Noodles', 'Omelette', 'Mushrooms', 'Caramel', 'Chocolate']

toppings = ['Cheese', 'Rice', 'Meatballs', 'Chips', 'Toast', 'Mash', 'Salad', 'Ice Cream', 'Quiche', 'Milk']

random_food = food[random.randint(0, len(food))]

random_topping = toppings[random.randint(0, len(toppings))]

print('For today dinner is ' + random_food + ' and ' + random_topping + '!')
