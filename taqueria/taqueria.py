menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order = []

def total_cost():
    total_cost = sum(menu[item] for item in order)
    print(f"Total: ${total_cost:.2f}" )

try:
    while True:
        item = input("Item:").strip().title()

        if item in menu:
            order.append(item)
            total_cost()

except EOFError:
    total_cost()
