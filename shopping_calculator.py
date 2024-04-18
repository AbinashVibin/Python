def calculate_discounted_price(item):
    discount_percentage = 0.05
    return item- (item* discount_percentage)

def main():
    total_cost = 0
    items = []

    numb_items = int(input("Enter the number of items purchased: "))
