from datetime import date, datetime
import sys
import inflect


def get_birth_date(birth_date_str):
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        current_date = date.today()

        if birth_date > current_date:
            raise ValueError

        return birth_date

    except:
        sys.exit("Invalid date")

def calculate_age_in_minutes(birth_date,current_date):
    age_in_days = (current_date - birth_date).days
    age_in_minutes = age_in_days * 24 * 60
    return round(age_in_minutes)

def convert_to_words(age_in_minutes):
    p = inflect.engine()
    age_in_words = p.number_to_words(age_in_minutes, andword="")
    return age_in_words

def main():

    birth_date_str = input("Date of Birth: ")
    birth_date = get_birth_date(birth_date_str)
    current_date = date.today()

    age_in_minutes = calculate_age_in_minutes(birth_date,current_date)
    age_in_words = convert_to_words(age_in_minutes).capitalize()

    print(f"{age_in_words} minutes")

if __name__ == "__main__":
    main()
