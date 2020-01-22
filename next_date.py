def generate_next_date(day,month,year):
    next_day = 0
    next_month = 0
    next_year = 0
    if month in [1,3,5,7,8,10,12]:
        if day<31:
            next_day=day+1
            next_year = year
        elif day==31:
            next_day = 1
            if month == 12:
                next_year = year+1
                next_month = 1
            else:
                next_month = month+1
                next_year = year
                
    elif month in [2,4,6,9,11]:
        if month == 2:
            if (year % 400 or year%4) ==0:
                if day < 29:
                    next_day = day+1
                elif day==29:
                    next_day = 1
                    next_month = month+1
            else:
                if day < 28:
                    next_day = day+1
                elif day==28:
                    next_day = 1
                    next_month = month+1
        else:
            if day < 30:
                next_day=day+1
            elif day == 30:
                next_day =1
                next_month=month+1
        next_year = year      
    print(next_day,"-",next_month,"-",next_year)


day = input('enter day: ')
month = input('enter month: ')
year = input('enter year: ')
generate_next_date(day,month,year)
