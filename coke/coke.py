def main():


    amount=int(50)
    tot_in= 0
    change= 0
    print("Amount Due:",amount)
    while tot_in < amount:

        coin_ins = coin()

        tot_in += coin_ins
        r_amount=amount-tot_in
        if r_amount== amount:
            print("Amount Due:",amount)
        elif r_amount > 0:
            print("Amount Due:",r_amount)
        else:
            change += -r_amount
            print("Change Owed:",change)
            break





def coin():
    amount=50

    while True:
        x=int(input("Insert Coin:"))

        if x==25 or x==10 or x==5:
            return x
        else:
            print("Amount Due:", amount)


main()