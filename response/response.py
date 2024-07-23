import validators

def is_valid_email(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

def main():
    email = input("What's your email address? ")
    result = is_valid_email(email)
    print(result)

if __name__ == "__main__":
    main()
