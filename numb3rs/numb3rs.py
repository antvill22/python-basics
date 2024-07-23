import re
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r'^(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}\.)(\d{1,3})$',ip)

    if match:
        first_part = match.group(1).strip(".")
        second_part = match.group(2).strip(".")
        third_part = match.group(3).strip(".")
        fourth_part = match.group(4)


        if (0 <= int(first_part) <= 255)and(0 <= int(second_part) <= 255)and(0 <= int(third_part) <= 255)and (0 <= int(fourth_part) <= 255):
            return True
    return False


if __name__ == "__main__":
    main()