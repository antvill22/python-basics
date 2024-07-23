import inflect
p = inflect.engine()
names=[]

try:
    while True:
        name=input("Name:").title()
        names.append(name)
except EOFError:
    list_name=p.join(names)
    print("Adieu, adieu, to",list_name)
