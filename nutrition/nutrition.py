fruits = [
    { "APPLE": 130},
    { "AVOCADO": 50},
    { "BANANA": 110},
    { "CANTALUPE": 50},
    { "GRAPEFRUIT": 60},
    { "GRAPES": 90},
    { "HONEYDEW MELON": 50},
    { "KIWIFRUIT": 90},
    { "LEMON": 15},
    { "LIME": 20},
    { "NECTARINE": 60},
    { "ORANGE": 80},
    { "PEACH": 60},
    { "PEAR": 100},
    { "PINEAPPLE": 50},
    { "PLUMS": 70},
    { "STRAWBERRY": 50},
    { "SWEET CHERRIES": 100},
    { "TANGERINE": 50},
    { "WATERMELON": 80},
]

fruit=input("Item:").upper()
for i in range(0,len(fruits)):
    if fruit in fruits[i]:
        print("Calories:",fruits[i][fruit])