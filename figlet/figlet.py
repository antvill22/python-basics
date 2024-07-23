import sys
import random
from pyfiglet import Figlet
from pyfiglet import FigletFont
figlet = Figlet()
figfonts=FigletFont.getFonts()
if len(sys.argv)<2:
    f=random.choice(figfonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    f= sys.argv[2]
    if f in figfonts:
        f= sys.argv[2]
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
try:
    figlet.setFont(font=f)
    s=input("Input:")
    print(figlet.renderText(s))
except:
     sys.exit("Invalid usage")