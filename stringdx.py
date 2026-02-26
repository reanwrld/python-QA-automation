order_string = " fire-balls , smoke cakes ,java pies , molten-milk "
order_string = order_string.strip()
food_items = order_string.split(",")
for i in range(len(food_items)):
    food_items[i] = food_items[i].strip()
cleaned_food_items = []
for food_item in food_items:
    cleaned = food_item
    cleaned = food_item.replace("-", " ")
    cleaned_food_items.append(cleaned)

print(cleaned_food_items)