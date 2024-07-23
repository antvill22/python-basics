import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = re.compile(r'(\d{1,2}):(\d{2})\s+(AM|PM)\s+to\s+(\d{1,2}):(\d{2})\s+(AM|PM)')
    pattern2=re.compile( r'(\d{1,2})\s+(AM|PM)\s+to\s+(\d{1,2})\s+(AM|PM)')
    pattern3=re.compile( r'(\d{1,2}):(\d{2})\s+(AM|PM)\s+to\s+(\d{1,2})\s+(AM|PM)')
    pattern4=re.compile( r'(\d{1,2})\s+(AM|PM)\s+to\s+(\d{1,2}):(\d{2})\s+(AM|PM)')

    match = pattern.search(s)
    match2= pattern2.search(s)
    match3= pattern3.search(s)
    match4= pattern4.search(s)


    if match:
        start_hour=match.group(1)
        start_min=match.group(2)
        start_period=match.group(3)
        end_hour=match.group(4)
        end_min=match.group(5)
        end_period = match.group(6)
    elif match2:
        start_hour=match2.group(1)
        start_min=0
        start_period=match2.group(2)
        end_hour=match2.group(3)
        end_min=0
        end_period = match2.group(4)
    elif match3:
        start_hour=match3.group(1)
        start_min=match3.group(2)
        start_period=match3.group(3)
        end_hour=match3.group(4)
        end_min=0
        end_period = match3.group(5)
    elif match4:
        start_hour=match4.group(1)
        start_min=0
        start_period=match4.group(2)
        end_hour=match4.group(3)
        end_min=match4.group(4)
        end_period = match4.group(5)
    else:
        raise ValueError("Invalid time format")

    start_hour = int(start_hour)
    end_hour = int(end_hour)

    if start_period == 'PM':
        if start_hour!=12:
            start_hour += 12
        else:
            start_hour=12
    else:
        if start_hour==12:
            start_hour=0

    if end_period == 'PM':
        if end_hour!=12:
            end_hour += 12
        else:
            end_hour=12
    else:
        if end_hour==12:
            end_hour=0

    if not (0 <= start_hour <= 23) or not (0 <= end_hour <= 23) or not (0 <= int(start_min) <= 59) or not (0 <= int(end_min) <= 59):
        raise ValueError("Invalid time")

    return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"


if __name__ == "__main__":
    main()
