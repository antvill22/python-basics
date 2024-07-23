def main():

    frac = input("Fraction: ").strip()

    r = convert(frac)
    percentage=gauge(r)
    print(percentage, sep="", end="")



def convert(fraction):
    while True:

        try:
            x_str, y_str = fraction.split('/')
            x = int(x_str)
            y = int(y_str)
            div= x/y
            if x<=y:
                perc=int(div * 100)
                return perc
            else:
                frac = input("Fraction: ").strip()
                pass
        except (ValueError,ZeroDivisionError):
            raise


def gauge(percentage):

    if percentage <=1 :
        percentage= 'E'
        return percentage
    elif percentage >=99 :
        percentage= 'F'
        return percentage
    else:
            perc=(str(percentage) + '%')
            return perc


if __name__ == "__main__":
    main()