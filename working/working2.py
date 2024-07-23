import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = re.compile(r'(\d{1,2}):?(\d{2})?\s*(AM|PM)\s*to\s*(\d{1,2}):?(\d{2})?\s*(AM|PM)')

    match = pattern.search(s)

    if match:
        groups = match.groups()[:6]
        if groups[1] and groups[4]:
            start_hour, start_min, start_period, end_hour, end_min, end_period = groups
        elif not groups[1] and groups[4]:
            start_hour, start_period, end_hour, end_min, end_period = groups
            start_min = 0
        elif groups[1] and not groups[4]:
            start_hour, start_min, start_period, end_hour, end_period = groups
            end_min = 0
        else:
            start_hour, start_period, end_hour, end_period = groups
            start_min = 0
            end_min = 0

        start_hour = int(start_hour)
        end_hour = int(end_hour)

        if start_period == 'PM':
            start_hour += 12
        if end_period == 'PM':
            end_hour += 12

        if not (0 <= start_hour <= 23) or not (0 <= end_hour <= 23) or not (0 <= int(start_min) <= 59) or not (0 <= int(end_min) <= 59):
            raise ValueError("Invalid time")

        return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"

    raise ValueError("Invalid time format")

if __name__ == "__main__":
    main()
