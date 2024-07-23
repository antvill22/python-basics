def main():
    time=input("What time is it?")

    hours_decimal=convert(time)
    if 7.0<= hours_decimal <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours_decimal <=13.0:
        print("lunch time")
    elif 18.0 <= hours_decimal <= 19.0:
        print("dinner time")


def convert(time):
    h,m =time.split(":")
    hours=float(h)
    minutes=float(m)

    if  0 <= hours <= 23 and 0 <= minutes <=59:
        hours_decimal=hours+(minutes/60)
        return hours_decimal


if __name__ == "__main__":
    main()