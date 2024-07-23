def main():
    p = input("Plate: ").upper()
    if is_valid(p):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    def max_min():
        return (2 <= len(s) <= 6)

    def two_l():
        return s[0:2].isalpha()

    def let():
        return s.isalpha()

    def let_num():
        return s.isalnum()

    def zero():
        for c in s:
            if c.isdigit():
                i = s.index(c)
                if s[i].isdigit() and int(c) != 0:
                    return True
                else:
                    return False

    def num_fin():
        rev_s = s[::-1]
        i=0
        while i<len(rev_s):
            if  i+3>len(rev_s):
                break



            if rev_s[i].isalpha() and rev_s[i+1].isdigit():
                c=False
                return c
            elif rev_s[i].isdigit() and rev_s[i+1].isalpha() and rev_s[i+2].isdigit():
                c=False
                return c
            elif rev_s[i].isdigit() and rev_s[i+1].isalpha() and rev_s[i+2].isalpha() and rev_s[i+3].isdigit():
                c=False
                return c
            else:
                c=True
                return c


        i+=1


    return max_min() and two_l() and let_num() and num_fin() and (zero() or let())


if __name__ == "__main__":
    main()
