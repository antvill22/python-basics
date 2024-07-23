def main():
    p = input("Plate: ").upper()
    if is_valid(p):
        print("Valid")
    else:
        print("Invalid")

# maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
def max_min(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

#All vanity plates must start with at least two letters.
def two_l(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

#No periods, spaces, or punctuation marks are allowed.
def let(s):
     if s.isalpha():
        return True

def let_num(s):

    if s.isalnum():
        return True
    else:
        return False

#The first number used cannot be a ‘0’.
def zero(s):
    for c in s:
        if c.isdigit():
              i=s.index(c)
              if s[i].isdigit() and int(c) != 0:
                  return True
              else:
                  return False

#Numbers cannot be used in the middle of a plate; they must come at the end.
def num_fin(s):
    rev_s = ""
    for i in range(len(s)-1 , -1, -1):
        rev_s += s[i]
    for i in range(len(rev_s)-1):
        if rev_s[i].isalpha() and rev_s[i+1].isdigit():
            return False
        elif rev_s[i].isdigit() and rev_s[i+1].isalpha() and rev_s[i+2].isdigit():
            return False
        elif rev_s[i].isdigit() and rev_s[i+1].isalpha() and rev_s[i+2].isalpha() and rev_s[i+3].isdigit():
            return False
        else:
            return True

def is_valid(s):
    return(max_min(s) and two_l(s) and let_num(s)  and num_fin(s) and (zero(s) or let(s)))

main()
