x= input("Greeting:").strip().casefold()
y=0
if y!=x.find("hello") and x.startswith("h"):
    print("$20")
elif y==x.find("hello"):
    print("$0")
else:
    print("$100")
