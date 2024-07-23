months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]




def change(date):
     try:
        month, day, year = date.split("/")
        day = int(day)
        year = int(year)
        month_num= int(month)
        if 1 <= month_num <= 12 and 1 <= day <= 31:
            month_num = f"{month_num:02}"
            day = f"{day:02}"
            date = f"{year}-{month_num}-{day}"
            return date

     except:
          try:
               month, day, year = date.split(" ")
               day_find=day.find(",")
               if day_find > -1:
                   day_repl=day.strip(',')
               else:
                   return None
               day_num= int(day_repl)
               if month in months:
                   month_num = int(months.index(month))+1
               if 1 <= month_num <= 12 and 1 <= day_num <= 31:
                month_num = f"{month_num:02}"
                day_num = f"{day_num:02}"
                date = f"{year}-{month_num}-{day_num}"
                return date

               else:
                   return None


          except ValueError:
              return None




while True:
    Pre_date = input("Date:").strip()

    date = change(Pre_date)

    if date is not None:
        print(date, sep="",end="")
        break