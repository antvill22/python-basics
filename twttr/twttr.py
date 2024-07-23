twitter=input("Input:")
twttr=""
vocal=["A","a","E","e","I","i","O","o","U","u"]
for t in twitter:
    if t in vocal:
        twttr += t.strip('AaEeIiOoUu')
    else:
        twttr += t

print(f"Output:{twttr}")