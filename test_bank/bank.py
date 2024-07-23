import string
def main():
    greeting= input("Greeting:")
    v = value(greeting)
    print(f"${v}")



def value(greeting):

    punct = string.punctuation
    for c in punct:
        s = greeting.replace(c, "").strip().casefold()
    y=0
    if y!=s.find("hello") and s.startswith("h"):
        value = 20
        return value
    elif y==s.find("hello"):
        value = 0
        return value
    else:
        value = 100
        return value


if __name__ == "__main__":
    main()
