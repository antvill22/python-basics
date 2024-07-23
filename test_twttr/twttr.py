def main():
    word=input("Input:")
    short=shorten(word)
    print(f"{short}")



def shorten(word):
    twttr=""
    vocal=["A","a","E","e","I","i","O","o","U","u"]
    for t in word:
        if t in vocal:
            twttr += t.strip('AaEeIiOoUu')
        else:
            twttr += t
    return twttr




if __name__ == "__main__":
    main()
