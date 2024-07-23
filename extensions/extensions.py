x=input("File name:").casefold().strip()
if x.endswith(".gif"):
    print("image/gif")
elif x.endswith(".jpg") or x.endswith(".jpeg"):
    print("image/jpeg")
elif x.endswith(".png"):
    print("image/png")
elif x.endswith(".pdf"):
    print("application/pdf")
elif x.endswith(".txt"):
    y=x.removesuffix(".txt")
    print(f"text/{y}")
elif x.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")