import sys

if len(sys.argv)==2:
    f=sys.argv[1]
    if f.endswith(".py"):
        try:
            with open(f,"r") as file:
                lines= file.readlines()
                x=0
                for line in lines:
                    line= line.lstrip().rstrip()
                    if line.startswith("#") or line=="":
                        x=x
                    else:
                        x+=1
                print(x)
        except:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments ")
