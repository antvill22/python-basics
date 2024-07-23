import re

def main():
    print(parse(input("HTML: ")))

def parse(s):

    match = re.search(r'<iframe.*?src="(https?://(?:www\.)?youtube\.com/embed/([^"]+))".*?</iframe>', s)

    if match:
        video_id = match.group(2)
        youtu_be_url = f'https://youtu.be/{video_id}'
        return youtu_be_url
    else:
        return None

if __name__ == "__main__":
    main()
