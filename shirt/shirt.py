import sys,os
from PIL import Image,ImageOps

def r_o_s(before,after):
    try:
        img_before= Image.open(before)
        shirt = Image.open("shirt.png")


        img_before = ImageOps.fit(img_before,shirt.size)

        img_before.paste(shirt, shirt)

        img_before.save(after)
        sys.exit(0)

    except FileNotFoundError:
         sys.exit("Input does not exist")
if __name__=="__main__":
    if len(sys.argv)==3:
        before=sys.argv[1].casefold()
        after=sys.argv[2].casefold()
        before_path = os.path.splitext(before)
        after_path = os.path.splitext(after)
        valid_extensions = {".jpg", ".jpeg", ".png"}
        if (after_path[1] not in valid_extensions) or (before_path[1] not in valid_extensions):
            sys.exit("Invalid output")


        if (after_path[1]==before_path[1]):
             r_o_s(before,after)

        else:
            sys.exit("Input and output have different extensions")

    elif len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments ")
