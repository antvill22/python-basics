List= []

def sort_alpha():
    List.sort()
    previous_item = None
    for item in List:
        if item != previous_item:
            num = List.count(item)
            print(f"{num} {item}")
        previous_item = item



try:
    while True:
        item = input().strip().upper()
        List.append(item)


except EOFError:
    sort_alpha()
