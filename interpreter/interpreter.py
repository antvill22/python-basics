def cal_exp(x,y,z):
    if y== '+':
        return x + z
    elif y=='-':
        return x-z
    elif y=='*':
        return x*z
    elif y=='/':
        return x/z
    else:
        return None


x, y, z=input("Expression:").split(" ")


if x.isdigit() and z.isdigit() and y in ['+','-','*','/']:
                                         x=int(x)
                                         z=int(z)

r=cal_exp(x,y,z)
if r is not None:
    print(f"{r:.1f}")
else:
    print("Invalid input.")
