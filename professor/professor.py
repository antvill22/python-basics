import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    valid_levels=range(1,4)
    while True:
        try:
            level=int(input("Level:"))
            for i in valid_levels:
                if level==i:
                    return level
        except ValueError:
            pass


def generate_integer(level):
    score = 0
    math_problems = 10
    for _ in range(math_problems):
        if level == 1:
            max_one = 9
            x = random.randint(0, max_one)
            y = random.randint(0, max_one)
        elif level == 2:
            max_two = 99
            x = random.randint(10, max_two)
            y = random.randint(10, max_two)
        elif level == 3:
            max = 999
            x = random.randint(100, max)
            y = random.randint(100, max)
        else:
            raise ValueError

        r = x + y
        t=0
        while t<3:
            answer = input(f"{x} + {y} = ")
            try:
                answer=int(answer)
                if answer==r:
                    score +=1
                    break
                else:
                    t += 1
                    if t < 3:
                        print("EEE")
                    else:
                        print(f"{x}+{y}={r}")

            except ValueError:
                t+=1
                if t<3:
                    print("EEE")
                else:
                    print(f"{x} + {y} = {r}")


    print(score)


if __name__ == "__main__":
    main()