def calculate_total_cost(items):
    total= 0
    for item in items:
        total_cost += item['price']
    return total_cost

def apply_discount(items):
    for item in items:
        if item['name'][0].lower() in 'aeiou':
            item(input("Enter the number of items purchased: "))

    for _ in range(num_items):
        name = input("Enter the name of the item: ")
        price = float(input("Enter the price of the item: "))
        items.append({'name': name, 'price': price})

    apply_discount(items)
    total_cost = calculate_total_cost(items)
    print("Total cost after applyin